import csv
import time
import os

FILE_NAME = "tasks.csv"


def read_tasks(file_name):
    if not os.path.exists(file_name):
        return []

    with open(file_name, mode="r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def update_task_status_and_save(tasks, task_id, new_status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            break
    save_tasks_to_file(tasks)


def save_tasks_to_file(tasks):
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "timestamp", "status"])
        writer.writeheader()
        writer.writerows(tasks)


def show_processing_animation(task_id, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            print(f"\rProcessing task {task_id}{'.' * i}    ", end="", flush=True)
            time.sleep(0.5)
    print(f"\rProcessing task {task_id}... Done!    ", flush=True)


def get_task_to_process(tasks):
    for task in tasks:
        if task["status"] == "in_progress":
            print(f"Recovering task {task['id']}")
            return task

    for task in tasks:
        if task["status"] == "pending":
            return task
    return None


if __name__ == "__main__":
    print("Consumer started. Monitoring tasks...")

    while True:
        tasks = read_tasks(FILE_NAME)
        task_to_process = get_task_to_process(tasks)

        if task_to_process:
            task_id = task_to_process["id"]

            update_task_status_and_save(tasks, task_id, "in_progress")

            show_processing_animation(task_id, 30)

            update_task_status_and_save(tasks, task_id, "done")
        else:
            print("No pending tasks. Waiting...")

        time.sleep(5)
