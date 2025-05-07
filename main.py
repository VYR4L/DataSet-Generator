from pathlib import Path
from download_images import download_images
from gray_scale_converter import convert_to_gray, delete_images


ROOT_DIR = Path(__file__).parent

DOWNLOAD_DIR = ROOT_DIR / "images"
DOWNLOAD_DIR.mkdir(exist_ok=True)

CONVERT_DIR = ROOT_DIR / "gray_images"
CONVERT_DIR.mkdir(exist_ok=True)

URL = "https://thispersondoesnotexist.com/"


if __name__ == "__main__":
    # Download images
    download_images(URL, DOWNLOAD_DIR)

    # Convert images to grayscale
    convert_to_gray(DOWNLOAD_DIR, CONVERT_DIR)

    # Delete original images
    delete_images(DOWNLOAD_DIR)
