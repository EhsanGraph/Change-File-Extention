import os
from wand.image import Image

def convert_tiff_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".tiff") or filename.endswith(".tif"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            
            with Image(filename=input_file_path) as img:
                img.save(filename=output_file_path)
                
            print(f"Converted {filename} to PDF")

input_folder = "address 1"
output_folder = "address 2"

convert_tiff_to_pdf(input_folder, output_folder)
