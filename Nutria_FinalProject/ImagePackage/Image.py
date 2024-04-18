

#Image.py


from PIL import Image
import os

# Directory containing the image file
directory_path = r"C:\Users\zihao\git\Nutria_FinalProject\Nutria_FinalProject\ImagePackage"

# Image file name
image_filename = "Image1.jpg"

# Construct the full path to the image file
image_path = os.path.join(directory_path, image_filename)

# Open the image
image = Image.open(image_path)

# Display the image
image.show()
