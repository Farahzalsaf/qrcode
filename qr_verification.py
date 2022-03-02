import qrcode 

img = qrcode.make("https://github.com/Farahzalsaf")
img.save("qr_verification.png")