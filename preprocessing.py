import cv2
import os


def preprocess_image(img_path, output_dir):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Cannot load image: {img_path}")
        return

    os.makedirs(output_dir, exist_ok=True)

    # Median Blur
    median_blur = cv2.medianBlur(img, 3)
    cv2.imwrite(os.path.join(output_dir, "median_blur.png"), median_blur)

    # Gaussian Blur + Otsu Thresholding
    gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
    _, otsu_thresh = cv2.threshold(
        gaussian_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    cv2.imwrite(os.path.join(output_dir, "gaussian_otsu.png"), otsu_thresh)

    # Bilateral Filter + Otsu Thresholding
    bilateral_filter = cv2.bilateralFilter(img, 5, 75, 75)
    _, bilateral_otsu = cv2.threshold(
        bilateral_filter, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    cv2.imwrite(os.path.join(output_dir, "bilateral_otsu.png"), bilateral_otsu)

    # Median Blur + Otsu Thresholding
    median_otsu = cv2.medianBlur(img, 3)
    _, median_otsu = cv2.threshold(
        median_otsu, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    cv2.imwrite(os.path.join(output_dir, "median_otsu.png"), median_otsu)

    # Adaptive Threshold + Gaussian Blur
    gaussian_blur_adaptive = cv2.GaussianBlur(img, (5, 5), 0)
    adaptive_thresh_gaussian = cv2.adaptiveThreshold(
        gaussian_blur_adaptive,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )
    cv2.imwrite(
        os.path.join(output_dir, "adaptive_gaussian.png"), adaptive_thresh_gaussian
    )

    # Adaptive Threshold + Bilateral Filter
    bilateral_adaptive = cv2.bilateralFilter(img, 9, 75, 75)
    adaptive_thresh_bilateral = cv2.adaptiveThreshold(
        bilateral_adaptive,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )
    cv2.imwrite(
        os.path.join(output_dir, "adaptive_bilateral.png"), adaptive_thresh_bilateral
    )

    # Adaptive Threshold + Median Blur
    median_blur_adaptive = cv2.medianBlur(img, 3)
    adaptive_thresh_median = cv2.adaptiveThreshold(
        median_blur_adaptive,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )
    cv2.imwrite(os.path.join(output_dir, "adaptive_median.png"), adaptive_thresh_median)

    print(f"Preprocessing finished, results recorded in: {output_dir}")


if __name__ == "__main__":
    test_image_path = (
        r"C:\Users\gajda\Desktop\images\Okta-Captcha.png"
    )
    output_directory = "output_images"

    preprocess_image(test_image_path, output_directory)
