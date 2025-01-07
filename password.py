import random
import string

def generate_password(length=12, use_digits=True, use_special=True, use_uppercase=True, use_lowercase=True):
    """Generate a random password based on user preferences."""
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None
    
    # Define character pools
    digits = string.digits
    special = string.punctuation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    # Create the character pool based on user choices
    all_characters = ""
    if use_digits:
        all_characters += digits
    if use_special:
        all_characters += special
    if use_lowercase:
        all_characters += lower
    if use_uppercase:
        all_characters += upper
    
    # Ensure the character pool isn't empty
    if not all_characters:
        print("You must select at least one character type!")
        return None

    # Generate the password
    password = random.choices(all_characters, k=length)
    
    return ''.join(password)

# Input for desired password length and options
length = int(input("Enter the desired password length (minimum 6): "))
use_digits = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'

# Generate and display the password
password = generate_password(length, use_digits, use_special, use_uppercase, use_lowercase)

if password:
    print(f"Generated Password: {password}")
