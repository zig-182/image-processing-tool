import sys
import os
#Note: Library used to be called pillow
from PIL import Image

#Grab the input and output directories from the command line
jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

#Check if the output directory exists, if not, create it
#Note: This stops it being created multiple times if you run it again)
if not os.path.exists(png_folder):
    os.makedirs(png_folder)
    
#create a loop to go through each file in the input directory
for filename in os.listdir(jpg_folder):
#The following line avoids us having jpg and png in the file name
  png_filename = os.path.splitext(filename)[0]
  img = Image.open(f'{jpg_folder}{filename}')
  #added the / in case user doesn't enter it
  img.save(f'{png_folder}/{png_filename}.png', 'png')
  
  print(f"You've successfully converted {filename} to a PNG file!")