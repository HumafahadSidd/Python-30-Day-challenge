"""🚀 Challenge: Aisa Python program likhna hai jo user se ek sentence le aur usme jitne words hain, count kare! 🔢💡  

🔥 Example:  
📌 Input: "Python is amazing!"  
📌 Output: Total words: 3  
📌 Explaination: The sentence has 3 words."""

# Solution:
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Total words: {len(words)}")

"""Agar tumhe extra challenge chahiye, to same program ko aise modify karo ke words ko reverse order me print kare! 🔄  

📌 Example:  
🔹 Input: "I love Python"  
🔹 Output: "Python love I"  

"""
# Solution:
sentence2 = input("Enter a sentence: ")
words2 = sentence2.split()
words2.reverse()
print(" ".join(words2))