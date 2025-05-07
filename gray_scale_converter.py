from PIL import Image
import os


def convert_to_gray(input_dir, output_dir):
    for i, image_path in enumerate(input_dir.glob("*.jpg")):
        # Open the image file
        with Image.open(image_path) as img:
            # Convert the image to grayscale
            gray_img = img.convert("L")
            
            # Save the grayscale image to the output directory
            gray_img.save(output_dir / f"gray_face_{i}.jpg")
        

def delete_images(input_dir):
    for image_path in input_dir.glob("*.jpg"):
        os.remove(image_path)