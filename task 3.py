# Password Generator Program

import random      # Used to generate random characters
import string      # Contains letters, digits, symbols

print("===== PASSWORD GENERATOR =====")

# Ask user for password length
length = int(input("Enter desired password length: "))

# Combine all characters (letters + digits + symbols)
all_characters = string.ascii_letters + string.digits + string.punctuation

password = ""

# Generate random password
for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)
