import csv
import time
from datetime import datetime
import uuid

FILE_NAME = "tasks.csv"


def create_task(name: str):
    task_id = str(uuid.uuid4())
    task_data = {
        "id": task_id,
        "name": name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "pending",
    }
    return task_data


def save_task_to_file(task, file_name):
    with open(file_name, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "timestamp", "status"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(task)


if __name__ == "__main__":
    print("Producer started. Generating tasks...")
    task = create_task("rozmowa telefoniczna")
    save_task_to_file(task, FILE_NAME)
    print(f"Task created: {task}")
