"""📢 Day 6 – Daily Python Challenge 🐍
🚀 Challenge:
Aisa Python program likhna hai jo user se ek integer number lega aur uska binary (0s aur 1s) me conversion karega, phir check karega ke ye palindrome hai ya nahi! 🔄✨

🔥 Example:
📌 Input: 9
📌 Binary: 1001
📌 Output: Palindrome ✅

📌 Input: 13
📌 Binary: 1101
📌 Output: Not a Palindrome ❌
"""
num_user=int(input("Enter a number: "))
num_bin=bin(num_user)
num_bin=num_bin[2:]
if num_bin==num_bin[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
    