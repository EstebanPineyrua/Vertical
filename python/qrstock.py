import qrcode
from PIL import Image


data = "https://estebanpineyrua.github.io/Vertical/"


qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)


qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')


logo = Image.open("logo.png")


qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.25)
logo = logo.resize((logo_size, logo_size))


pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)


qr_img.save("qr_con_logo.png")

print("✅ Código QR con logo guardado como 'qr_con_logo.png'")
