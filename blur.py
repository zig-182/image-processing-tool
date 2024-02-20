import sys
import os
from PIL import Image, ImageFilter

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#This makes the image more or less blurry
blur_radius = 5

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    blurry_filename = os.path.splitext(filename)[0]
    output_path = os.path.join(output_folder, f"{blurry_filename}.jpg")

    # Open the image, apply a blur filter, and save in the output folder
    img = Image.open(input_path)
    blurry_img = img.filter(ImageFilter.BLUR).filter(ImageFilter.BLUR)
    blurry_img.save(output_path, 'JPEG')

    print(f"You've successfully applied a blur effect to {filename} and saved it in the {output_folder} folder.")
