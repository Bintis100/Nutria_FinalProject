#movie.py

import json
from cryptography.fernet import Fernet

file_path = '../Resources/TeamsAndEncryptedMessagesForDistribution - 001.json'

# Read the JSON file    
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the structure of the data
print("Nutria entry:", data['Nutria'])

#help(cryptography.fernet)
    
# Define the Fernet key
key = b'5cO4IoIiCYWy9oCnI8e2bKQYCGRCnp1TOw_4oApG9RE='

# Encrypted data
encrypted_data = "gAAAAABlTNM6y53q07FGQtScW71cj_nSCAnWc09gnlMCvd5XQrQ_jwXRKT1unh_Axc3PW7At7GBxUe28DNjGIWwb-wEWQ1x2Zw=="

# Initialize Fernet with the key
f = Fernet(key)

# Decrypt the data
decrypted_data = f.decrypt(encrypted_data.encode())

print('Decrypted data:', decrypted_data.decode())
