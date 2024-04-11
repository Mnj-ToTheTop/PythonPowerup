import qrcode
from PIL import Image

while True:
    print("Choices: 1. New QR\t2.Exit.")
    choice = int(input("Enter choice: "))
    if choice==1:
        info = input("Enter info: ")
        QR = qrcode.make(info)
        QR.save("QRcode.png")
        im = Image.open("QRcode.png")
        im.show()
    elif choice==2:
        print("Thank you")
        break
    else:
        print("Enter valid choice.")

        
