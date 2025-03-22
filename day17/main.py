"""
📢 Day 17 – Daily Python Challenge 🐍
🚀 Challenge: Create a QR Code Generator! 📱🔗

🔥 Requirements:
⿡ Take any text, URL, or message as input.
⿢ Generate a QR code for the input.
⿣ Save the QR code as an image file (e.g., qrcode.png).
⿤ The QR code should be scannable using any QR scanner app.

💡 Hint: Use the qrcode library in Python to generate QR codes easily!

"""

import qrcode

# Input
data = input("Enter the text, URL, or message: ")

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save QR Code
img.save("qrcode.png")

print("QR Code generated successfully!")

