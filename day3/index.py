"""📢 Day 3 – Daily Python Challenge 🐍
🚀 Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 🔢💡

🔥 Example:
📌 Input: 7
📌 Output: Yes, it's a prime number!
📌 Input: 10
📌 Output: No, it's not a prime number!
"""
# Solution:
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("No, it's not a prime number!")
            break
    else:
        print("Yes, it's a prime number!")
else:
    print("No, it's not a prime number!")