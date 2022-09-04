import validators
import qrcode
def generate_qrcode(link):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants. ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr001.png")
url1=input("enter the url: ")
if validators.url(url1)==True:
    print("valid URL")
    generate_qrcode(url1)
    print("image saved sucessfully")
else:
    print("input vaild url")
    exit()