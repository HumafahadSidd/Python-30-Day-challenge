"""📢 Day 10 – Daily Python Challenge 🐍
🚀 Challenge: "Anagram Checker" 🔄
Aaj ka challenge hai ek Anagram Checker banana! Tumhe ek Python program likhna hai jo do words compare kare aur check kare ke kya dono anagrams hain ya nahi. 🔍

🔥 Anagram Kya Hota Hai?
Agar do words ke letters same hoon lekin order different ho, to wo anagrams hote hain.
Example: "listen" aur "silent" anagrams hain, kyunki dono me same letters hain, bas order change hai. ✅

Task Requirements:
⿡ User se do words input lo.
⿢ Check karo ke dono words anagram hain ya nahi.
⿣ Result print karo:
"""

# Solution:
def anagram_checker(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
    
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if anagram_checker(word1, word2):
    print("Both words are Anagrams.")
else:
    print("Both words are not Anagrams.")
    