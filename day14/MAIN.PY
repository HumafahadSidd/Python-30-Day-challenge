"""📢 Day 14 – Daily Python Challenge 🐍
🚀 Challenge: Create a Text-Based Adventure Game where the user makes choices that impact the story! 🎮✨

🔥 Requirements:
⿡ Display a short intro story.
⿢ Give the player two choices at each step.
⿣ The choices should lead to different outcomes (win/lose/continue).
⿤ Keep it simple & interactive using input().

"""

# Solution:

def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You are in a dark room with two doors. Which door do you choose?")
    print("1. Door 1")
    print("2. Door 2")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("You enter a room filled with treasure! You win!")
    elif choice == "2":
        print("The door leads to a room filled with fire! You lose!")
    else:
        print("Invalid choice! Try again.")
        start_game()

start_game()
