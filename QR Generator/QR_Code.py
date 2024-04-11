import qrcode
from PIL import Image 

print("QR Code Generator")
info = input("Enter the info to store in QR: ")
qrcode.make(info)
image = qrcode.make(info) #QR is stored in image
image.save("QR_Code.png")
Image.open("QR_Code.png")
