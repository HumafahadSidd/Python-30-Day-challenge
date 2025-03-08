"""📢 Day 11 – Daily Python Challenge 🐍
🚀 Challenge: "Emoji Sentiment Analyzer" 🤖😊😢
Aaj ka challenge thoda fun + useful hone wala hai! Tumhe ek Python program likhna hai jo user ke message ko analyze kare aur uske andar emojis ki base pe mood detect kare! 🎭 💡

📌 Task Requirements:
⿡ User se ek sentence input lo.
⿢ Check karo ke usme emojis hain ya nahi.
⿣ Agar emoji hai to uska mood detect karo:

😊, 😃, 😍 → "Happy Mood!"
😢, 😭, ☹ → "Sad Mood!"
😡, 🤬, 😠 → "Angry Mood!"
😐, 😶, 🤔 → "Neutral Mood!"
⿤ Agar koi emoji nahi mila to bolo: "No emoji found, can't detect mood!"
"""

# Main Code
import emoji

def emoji_sentiment_analyzer():
    user_input = input("Enter a sentence: ")
    
    # Define mood categories
    happy_emojis = {"😊", "😃", "😍"}
    sad_emojis = {"😢", "😭", "☹"}
    angry_emojis = {"😡", "🤬", "😠"}
    neutral_emojis = {"😐", "😶", "🤔"}
    
    detected_moods = set()

    # Extract emojis from input and determine moods
    for char in user_input:
        if emoji.is_emoji(char):  # Checks if char is an emoji
            if char in happy_emojis:
                detected_moods.add("Happy Mood! 😊")
            elif char in sad_emojis:
                detected_moods.add("Sad Mood! 😢")
            elif char in angry_emojis:
                detected_moods.add("Angry Mood! 😡")
            elif char in neutral_emojis:
                detected_moods.add("Neutral Mood! 😐")

    # Output results
    if detected_moods:
        print("Detected Moods:", ", ".join(detected_moods))
    else:
        print("No emoji found, can't detect mood!")

# Example Usage
emoji_sentiment_analyzer()









































import emoji

def emoji_sentiment_analyzer():
    user_input = input("Enter a sentence: ")
    emojis = [char for char in user_input if char in emoji.UNICODE_EMOJI['en']]
    if emojis:
        mood = ""
        for emoji in emojis:
            if emoji in ["😊", "😃", "😍"]:
                mood = "Happy Mood!"
            elif emoji in ["😢", "😭", "☹"]:
                mood = "Sad Mood!"
            elif emoji in ["😡", "🤬", "😠"]:
                mood = "Angry Mood!"
            elif emoji in ["😐", "😶", "🤔"]:
                mood = "Neutral Mood!"
        print(mood)
    else:
        print("No emoji found, can't detect mood!")

emoji_sentiment_analyzer()

# Output:
# Enter a sentence: I am happy 😊