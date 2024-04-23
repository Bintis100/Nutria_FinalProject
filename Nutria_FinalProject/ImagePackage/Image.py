#Image.py


from PIL import Image
import os

# Directory containing the image file
json_file_path = '../Resources/image1.jpg'


# Image file name


# Construct the full path to the image file
image_path = os.path.join( json_file_path)

# Open the image
image = Image.open(image_path)

# Display the image
image.show()
