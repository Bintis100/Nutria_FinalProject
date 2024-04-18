#movie.py
import json
import cryptography.fernet 


# Path to the JSON file
file_path = '../Resources/TeamsAndEncryptedMessagesForDistribution - 001.json'

# Reading the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
print("Nutria entry:", data['Nutria'])

help(cryptography.fernet)
