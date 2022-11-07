from pyqrcode import QRCode
import pyqrcode
import png

website = "www.google.co.in"

url = pyqrcode.create(website)

url.svg("GoogleQRCode.svg", scale = 8)

url.png("GoogleQRCode.png", scale = 6)
