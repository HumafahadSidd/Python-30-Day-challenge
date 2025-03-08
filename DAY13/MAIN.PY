"""📢 Day 13 – Daily Python Challenge 🐍  

🚀 Challenge: Build a Simple Encryption & Decryption Tool using Python! 🔒✨  

 🔹 Task:  
1. Take a message from the user.  
2. Encrypt the message using a simple Caesar Cipher (shift letters forward by 3).  
3. Decrypt the message back to its original form.  

"""

# Solution:

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

text = input("Enter the message: ")
s = 3
print("Original Message: ", text)
encrypted = encrypt(text, s)
print("Encrypted Message: ", encrypted)
decrypted = decrypt(encrypted, s)
print("Decrypted Message: ", decrypted)