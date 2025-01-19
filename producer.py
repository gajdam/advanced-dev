import requests
from flask import Flask, request, jsonify
import pika
import uuid
import os
import json
from pathlib import Path

from tensorboard.summary.v1 import image

DOWNLOADS_FOLDER = Path.home() / "Downloads"
app = Flask(__name__)


def new_task(task_id: str, image_path):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="image_queue", durable=True)

    channel.basic_publish(
        exchange="",
        routing_key="image_queue",
        body=f"{task_id}|{image_path}",
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print(f" [x] Sent {task_id}")
    connection.close()


def generate_task_id() -> str:
    return str(uuid.uuid4())


def is_task_in_queue(task_id, queue_name="image_queue"):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    try:
        queue = channel.queue_declare(queue=queue_name, passive=True)
        message_count = queue.method.message_count
        if message_count > 0:
            for method_frame, properties, body in channel.consume(queue_name):
                task_data = body.decode("utf-8").split("|")
                task_id_in_queue = task_data[0]
                if task_id_in_queue == task_id:
                    return True
    except pika.exceptions.ChannelClosedByBroker:
        return False

    return False


def get_number_of_people_from_file(task_id, output_dir=r"./processed_images"):
    for filename in os.listdir(output_dir):
        if task_id in filename:
            try:
                task_id_from_filename, file_extension = filename.rsplit("-", 1)

                number_of_people_str, extension = file_extension.split(".", 1)
                number_of_people = int(number_of_people_str)

                return number_of_people
            except ValueError:
                return None
    return None


def download_image(url):
    try:
        response = requests.get(url)

        response.raise_for_status()

        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading image: {e}")
        return None


@app.route("/get-people-count", methods=["GET"])
def get_image():
    image_path = request.args.get("image_path")

    if not image_path:
        return jsonify({"error": "No image path provided"}), 400

    if not os.path.isfile(image_path):
        return jsonify({"error": "Image does not exist"}), 404

    task_id = generate_task_id()

    new_task(task_id, image_path)

    return jsonify({"task_id": task_id}), 202


@app.route("/get-people-count-url", methods=["GET"])
def get_image_url():
    image_url = request.args.get("image_url")

    if not image_url:
        return jsonify({"error": "No image url provided"}), 400

    try:
        task_id = generate_task_id()

        new_task(task_id, image_url)
        return jsonify({"task_id": task_id}), 202

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/process-image", methods=["POST"])
def process_image_endpoint():
    task_id = generate_task_id()

    file = request.files["file"]
    image_data = file.read()

    new_task(task_id, image_data)

    return jsonify({"task_id": task_id}), 202


@app.route("/task-status", methods=["GET"])
def task_status():
    task_id = request.args.get("task_id")

    if is_task_in_queue(task_id):
        return jsonify({"task_id": task_id, "status": "pending"})

    number_of_people = get_number_of_people_from_file(task_id)
    if number_of_people is not None:
        return jsonify(
            {"task_id": task_id, "status": "done", "people_count": number_of_people}
        )

    return jsonify({"task_id": task_id, "status": "not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
