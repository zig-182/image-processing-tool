import sys
import os
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    bw_filename = os.path.splitext(filename)[0]
    output_path = os.path.join(output_folder, f"{bw_filename}.jpg")

    # Open the image, convert to black and white, and save in the output folder
    img = Image.open(input_path).convert('L')
    img.save(output_path, 'JPEG')

    print(f"You've successfully converted {filename} to black and white and saved it in the blackandwhite folder.")
