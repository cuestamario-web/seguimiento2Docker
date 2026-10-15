import os

import qrcode


def mostrar(evento):
    url = os.getenv("URL_INSCRIPCION", "https://eam.edu.co")
    print(f"INSCRIPCIONES - {evento}")
    print(f"Escanea el código para inscribirte: {url}")
    qr = qrcode.QRCode(border=1)
    qr.add_data(url)
    qr.print_ascii(invert=True)
