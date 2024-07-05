# QR Code Generator using PYTHON
'''
First we have to install pyqrcode using CMD Prompt

pip install pyqrcode

also install

pip install pypng
'''
import pyqrcode
import png
from pyqrcode import QRCode

link = "https://www.amazon.fr/"

url = pyqrcode.create(link)
url.svg("myqr.svg",scale = 8)
url.png("myqr.png",scale = 6)
