import qrcode
import io
import base64

def generate_qr_code_link(text: str) -> str:
    """
    Tạo QR code base64 từ 1 link/text
    """
    qr = qrcode.QRCode(version=1, box_size=5, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    base64_str = base64.b64encode(byte_im).decode("utf-8")
    return f"data:image/png;base64,{base64_str}"
