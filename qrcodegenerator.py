import qrcode
import image #3demo
## this is a example
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5,
)

data = "https://www.youtube.com/watch?v=HIcSWuKMwOw&pp=ygUJcmljayByb2xs"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color ="white")
img.save("test.png")
