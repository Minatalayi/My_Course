import qrcode

name=input("please enter your name: ")
phone_number=input("please enter your phone number: ")

img=qrcode.make(name)
img.save("qrcode.n.png")

img=qrcode.make(phone_number)
img.save("qrcode.ph.png")