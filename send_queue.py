import os
import requests


def send_images_to_api(folder_path, endpoint_url):
    all_files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    if not all_files:
        print("Folder nie zawiera plików.")
        return

    images_to_send = 1000
    sent_count = 0
    file_index = 0

    while sent_count < images_to_send:
        image_name = all_files[file_index]
        image_path = os.path.join(folder_path, image_name)

        params = {"image_path": image_path}

        try:
            response = requests.get(endpoint_url, params=params)

            if response.status_code == 202:
                print(f"[{sent_count + 1}/1000] Wysłano obraz: {image_name}")
                sent_count += 1
            else:
                print(
                    f"Błąd podczas wysyłania obrazu {image_name}: {response.status_code}, {response.text}"
                )
        except Exception as e:
            print(f"Wyjątek podczas wysyłania obrazu {image_name}: {e}")

        file_index = (file_index + 1) % len(all_files)


folder_path = r"C:\Users\gajda\Desktop\images-test"
endpoint_url = "http://localhost:5000/get-people-count"

send_images_to_api(folder_path, endpoint_url)
