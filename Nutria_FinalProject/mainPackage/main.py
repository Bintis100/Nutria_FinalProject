# Name: Binta Drammeh, Ruolin Chen, Josh Halbakken 
# email: Drammeba@mail.uc.edu, chenr9@mail.uc.edu, halbakjc@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23rd, 2024
# Course/Section: IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt encrypted location and movie name using text files and cryptography 
# Citations:#https://www.tutorialspoint.com/how-to-encrypt-and-decrypt-data-in-python
# Anything else that's relevant: 

#main.py

from moviePackage import movie
from ImagePackage import Image
from mainPackage import Location

if __name__ == "__main__":
    # Display the image
    Image.image.show()  # Assuming the image has been opened and can be directly accessed like this

    # Decrypt and print the location information
    Location.main()

    
