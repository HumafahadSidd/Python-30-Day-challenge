"""
📢 Day 9 – Daily Python Challenge 🐍
🚀 Challenge: "Password Strength Checker" 🔐
Aaj ka challenge hai ek password strength checker banana! Tumhe ek Python program likhna hai jo user ke diye gaye password ki strength analyze kare aur bata sake ke password weak, moderate ya strong hai! 💪🔑

🔥 Requirements:
1️⃣ User se password input lo.
2️⃣ Check karo ke password kitna strong hai:

Weak: Agar password 6 characters se chhota hai ya sirf alphabets hain.

Moderate: Agar password 8+ characters ka hai lekin koi special character nahi hai.

Strong: Agar password 8+ characters, uppercase, lowercase, number, aur special character sab kuch contain karta hai.

3️⃣ User ko batao ke password kis category me hai.

📌 Example:
Enter your password: abc123  
Password Strength: Weak ❌  

Enter your password: PythonRocks99  
Password Strength: Moderate ⚠  

Enter your password: P@ssw0rd2024!  
Password Strength: Strong ✅  

"""
# Solution:
user_input=input("Enter your password: ")

import re

def password_strength(password):
    if len(password)<6 or password.isalpha():
        return "Weak ❌"
    
    elif len(password)>=8 and not re.search("[!@#$%^&*()_+{}|:<>?]", password):
        return "Moderate ⚠"    
    elif len(password)>=8 and re.search("[!@#$%^&*()_+{}|:<>?]", password) and re.search("[A-Z]", password) and re.search("[a-z]", password) and re.search("[0-9]", password):
        return "Strong ✅"
    else:
        return "Weak ❌"
    
print(f"Password Strength: {password_strength(user_input)}")

# Output:
# Enter your password: abc123
# Password Strength: Weak ❌

# Enter your password: PythonRocks99
# Password
# Strength: Moderate ⚠

# Enter your password: P@ssw0rd2024!
# Password Strength: Strong ✅

# Enter your password: Python
# Password Strength: Weak ❌