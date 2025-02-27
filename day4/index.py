"""Day 4 – Daily Python Challenge 🐍
🚀 Challenge:Write a Python program that converts numbers into words! 🔢➡🔡

🔥Example:
📌 Input: 123
📌 Output: "One Hundred Twenty-Three"

📌 Input: 5067
📌 Output: "Five Thousand Sixty-Seven"

"""
# Solution:
valueToCOnverted=input("Enter the number to be converted to words: ")

def convertToWords(valueToCOnverted):
    # Define the numbers
    numbers = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # Define the suffixes
    suffixes = ["", "Thousand", "Million", "Billion"]

    # Define the function
    def convert(n, index):
        if n == 0:
            return ""
        elif n < 20:
            return numbers[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + convert(n % 10, 0)
        else:
            return numbers[n // 100] + " Hundred " + convert(n % 100, 0)

    # Define the main function
    def convertToWords(n):
        if n == 0:
            return "Zero"
        result = ""
        for i in range(len(suffixes)):
            if n % 1000 != 0:
                result = convert(n % 1000, i) + suffixes[i] + " " + result
            n //= 1000
        return result.strip()

    # Return the result
    return convertToWords(int(valueToCOnverted))

# Print the result
print(convertToWords(valueToCOnverted))