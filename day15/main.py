"""
📢 Day 15 – Daily Python Challenge 🐍
🚀 Challenge: Create a Random Password Generator using Python! 🔐✨

🔥 Requirements:
⿡ Generate a secure password of a given length.
⿢ Include uppercase, lowercase, numbers, and special characters.
⿣ Ensure the password is randomly generated every time.
⿤ Allow users to input the desired password length.

"""
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))    
    return password

if __name__ == '__main__':
    length = int(input("Enter the length of the password: "))
    print(generate_password(length))

