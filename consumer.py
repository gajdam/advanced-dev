from io import BytesIO

import pika
import cv2
import numpy as np
import os
from urllib.parse import urlparse
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="image_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

output_folder = "processed_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def is_path(input_str):
    try:
        parsed = urlparse(input_str)
        if all([parsed.scheme, parsed.netloc]):
            return "url"
    except ValueError:
        pass

    if os.path.exists(input_str) or os.path.isabs(input_str):
        return "path"
    return "code"


def process_image(image_path, task_id):
    print(image_path)

    if is_path(image_path) == "url":
        response = requests.get(image_path, timeout=10)
        if response.status_code != 200:
            print(f"Error: Failed to download image from {image_path}")
            return None
        image_bytes = BytesIO(response.content)
        frame = cv2.imdecode(
            np.frombuffer(image_bytes.read(), np.uint8), cv2.IMREAD_COLOR
        )
    elif is_path(image_path) == "path":
        frame = cv2.imread(image_path)
    else:
        image_bytes = BytesIO(image_path)
        frame = cv2.imdecode(
            np.frombuffer(image_bytes.read(), np.uint8), cv2.IMREAD_COLOR
        )

    # frame = cv2.resize(frame, (640, 480))

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    boxes, weights = hog.detectMultiScale(frame, winStride=(2, 2), scale=1.05)
    number_of_people = len(boxes)

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for xA, yA, xB, yB in boxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    extension = os.path.splitext(image_path)[1]
    output_filename = f"{task_id}-{number_of_people}{extension}"
    output_path = os.path.join(output_folder, output_filename)

    cv2.imwrite(output_path, frame)

    print(
        f"Processed {task_id}: {number_of_people} people detected, saved to {output_path}"
    )
    return number_of_people


def callback(ch, method, properties, body):
    message = body.decode("utf-8")

    if "|" not in message:
        print(f"Invalid message format: {message}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    task_id, image_path = message.split("|", 1)

    print(f" [x] Received image: {image_path} with task id: {task_id}")

    number_of_people = process_image(image_path, task_id)

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f" [x] Done processing image: {image_path} with task id: {task_id}")


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="image_queue", on_message_callback=callback)

print(" [*] Waiting for messages...")
channel.start_consuming()
