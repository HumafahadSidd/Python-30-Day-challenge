"""
📢 Day 8 – Daily Python Challenge 🐍  

🚀 Challenge: 
Aaj ka challenge "Number Guessing Game" hai! 🎯 Tumhe ek Python program likhna hai jo ek random number (1-100) generate kare aur user ko us number ko guess karne ka chance de! 💡🔢  

🔥 Requirements: 
⿡ Random number generate karein (1-100 ke beech).
⿢ User se guess input lein.  
⿣ Agar guess sahi ho to "Congratulations! You guessed it right!" print karein. 
⿤ Agar galat ho to batao ke number chhota hai ya bada.  
⿥ User ko multiple attempts milne chahiye.

📌  
"""
import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1

            if guess == number:
                print(f"Congratulations! You guessed it right! It took you {attempts} attempts.")
                break
            elif guess < number:
                print("The number is greater than your guess.")
            else:
                print("The number is smaller than your guess.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guess_number()



import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed it right! It took you {attempts} attempts.")
            break
        elif guess < number:
            print("The number is greater than your guess.")
        else:
            print("The number is smaller than your guess.")

if __name__ == "__main__":
    guess_number()
