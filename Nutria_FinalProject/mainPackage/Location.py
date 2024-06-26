#Location.py
import json

def decrypt_location(indices, text_file_path):
    """
    Decrypts a list of indices by mapping them to lines in a specified text file.

    Args:
    indices (list of str): Encrypted indices pointing to lines in the text file.
    text_file_path (str): Path to the text file that contains the words.

    Returns:
    str: A decrypted message constructed from words found at specified line numbers.
    """
    # List to hold the decrypted words
    decrypted_words = []

    # Open the text file and read lines based on encrypted indices
    with open(text_file_path, 'r') as text_file:
        lines = text_file.readlines()  # Read all lines at once to avoid multiple I/O operations(idk either, but it stops an error)

        # For each index in the encrypted data, find the corresponding line in the text file
        for index in indices:
            # Convert index to integer
            line_number = int(index) 
            try:
                # Append the word 
                decrypted_words.append(lines[line_number].strip())
            except IndexError:
                # Handle the case where the line number is out of range
                decrypted_words.append(f"<Line {line_number} out of range>")

    # Join all the words to form the decrypted message
    decrypted_message = ' '.join(decrypted_words)
    return decrypted_message

def main():
    """
    Main function to read encrypted data, decrypt it using a text file, and print the result.
    """
    # Path to the JSON file
    json_file_path = '../Resources/EncryptedGroupHints Spring 2024 Section 001-1.json'
    # Path to the text file containing words
    text_file_path = '../Resources/UCEnglish.txt'

    # Read the JSON file and extract the 'Nutria' entry (encrypted numbers)
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        encrypted_numbers = data['Nutria']

    # Decrypt the message using the encrypted numbers and the text file
    decrypted_message = decrypt_location(encrypted_numbers, text_file_path)
    print("Decrypted Nutria entry:", decrypted_message)

