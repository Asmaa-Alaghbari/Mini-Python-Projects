# python3 -m venv venv
# venv\Scripts\activate
# pip install qrcode

import qrcode

url = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(url)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")
