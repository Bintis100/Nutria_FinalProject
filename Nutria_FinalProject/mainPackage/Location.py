#location.py
import json

# Path to the JSON file
file_path = '../Resources/EncryptedGroupHints Spring 2024 Section 001-1.json'

# Reading the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Check if 'Nutria' exists in the data and print it
if 'Nutria' in data:
    print("Nutria entry:", data['Nutria'])
else:
    print("Entry 'Nutria' not found in the JSON data.")