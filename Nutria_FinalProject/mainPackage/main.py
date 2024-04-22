# main.py
from moviePackage import movie
from ImagePackage import Image
from mainPackage import Location

if __name__ == "__main__":
    # Display the image
    Image.image.show()  # Assuming the image has been opened and can be directly accessed like this

    # Decrypt and print the location information
    Location.main()

    # Print decrypted data from the movie module
    # Since movie.py prints its output directly upon import, we will adjust it to work with a function instead
    
