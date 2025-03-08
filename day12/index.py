""" Day 12 – Daily Python Challenge 🐍

🎯 Challenge: A Password Strength Checker banao jo user se ek password le aur uski strength analyze kare. 💡  

🔑 Rules:
✔ Weak Password: < 6 characters
✔ Medium Password: 6-10 characters, at least one digit  
✔ Strong Password: > 10 characters, at least one uppercase, one digit, and one special character

🔥 Example:
📌 Input: "Python123"  
📌 Output: "Strength: Medium"  
"""
def password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif 6 <= len(password) <= 10 and any(char.isdigit() for char in password):
        return "Medium"
    elif len(password) > 10 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(not char.isalnum() for char in password):
        return "Strong"
    else:
        return "Weak"

password = input("Enter your password: ")
print(password_strength(password))

