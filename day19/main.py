"""
📢 Day 19 – Daily Python Challenge 🐍
🚀 Challenge: Image to ASCII Art Converter 🎨🖼

🔥 Project Goal: Convert an image into ASCII art using Python! The program should take an image as input and generate an ASCII representation of it using different characters.

📌 Features to Implement:
✅ Load an Image: Use PIL (Pillow) to open an image.
✅ Resize & Convert to Grayscale: Make sure the image is small enough to be represented in ASCII.
✅ Map Pixels to Characters: Use ASCII characters (@ # * + - .) to represent different shades.
✅ Output ASCII Art: Print the ASCII representation in the console or save it to a file.


"""

# Importing the required libraries
from PIL import Image

# Defining the ASCII characters
ASCII_CHARS = '@%#*+=-:. '

# Resize the image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert the image to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str

# Main function

def main(image_path, new_width=100):
    try:
        # Open the image
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Resize the image
    image = resize_image(image)

    # Convert the image to grayscale
    image = grayify(image)

    # Convert pixels to ASCII
    ascii_str = pixels_to_ascii(image)

    # Format the ASCII string
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i + new_width] + "\n"

    # Print the ASCII art
    print(ascii_img)

# Run the main function
if __name__ == "__main__":
    image_path = "./image.jpeg"
    main(image_path)

