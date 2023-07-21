import random
import string

# Define the function to generate a password
def generate_password(length):
    # Define the possible characters that can be used in the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation.replace("'", "").replace('"', '').replace('\\', '').replace('`', '')
    # Removing some special characters to avoid issues with SQL queries and shell commands
    password_characters = letters + digits + symbols

    # Generate a random password by repeatedly choosing a random character from the password_characters string
    password = ''.join(random.choice(password_characters) for i in range(length))

    # Return the generated password
    return password

# Ask the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate a random password of the desired length using the generate_password function
password = generate_password(password_length)

# Print the generated password to the console
print("Your randomly generated password is:", password)
