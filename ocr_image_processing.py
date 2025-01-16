import cv2
import pytesseract
import os


def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    return image


def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def extract_text(image):
    return pytesseract.image_to_string(image)


def process_image(image_path):
    image = load_image(image_path)
    if image is None:
        return None

    gray_image = convert_to_gray(image)
    cleaned_image = remove_noise(gray_image)

    text = extract_text(cleaned_image)

    return text


if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
    folder_path = r"./images"

    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)
        extracted_text = process_image(image_path)

        if extracted_text:
            print("Detected text: ")
            print(extracted_text)
        else:
            print("Failed to detect text")
