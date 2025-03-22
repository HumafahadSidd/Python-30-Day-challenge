"""
🐍 Daily Python Challenge – Day 20 🎉  

🚀 Milestone Reached! Humne 20 din complete kar liye hain! Aaj ka challenge kuch khaas hone wala hai. 😎  

📝 Challenge: Python Flashcards App  
Ek Flashcards App banao jo programming concepts ya kisi bhi topic ke liye ho sakti hai. App user ko ek question show kare, aur jab wo "Show Answer" dabaye, usay correct answer display ho.  

🔹 Features: 
✅ User se question aur answer input lena  
✅ Ek random question display karna  
✅ "Show Answer" button pe answer reveal hona  
✅ Python dictionaries ya JSON ka use karna  
"""

import tkinter as tk
from tkinter import messagebox
import random

class FlashcardsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcards App")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        self.questions = {
            "What is the capital of India?": "New Delhi",
            "What is the capital of USA?": "Washington D.C.",
            "What is the capital of Japan?": "Tokyo",
            "What is the capital of Australia?": "Canberra",
            "What is the capital of France?": "Paris"
        }

        self.question_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=20)

        self.answer_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.answer_label.pack(pady=20)

        self.show_answer_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack(pady=20)

        self.new_question()

    def new_question(self):
        self.question_label.config(text=random.choice(list(self.questions.keys())))
        self.answer_label.config(text="")

    def show_answer(self):
        question = self.question_label.cget("text")
        answer = self.questions[question]
        self.answer_label.config(text=answer)



if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()