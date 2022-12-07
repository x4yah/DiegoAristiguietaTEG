import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import VerticalGradiantColorMask

def banner():
    print('''
  █████   ██▀███    ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄      ▓█████▄  ▒█████   ██▀███  
▒██▓  ██▒▓██ ▒ ██▒ ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒
▒██▒  ██░▓██ ░▄█ ▒▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒
░██  █▀ ░▒██▀▀█▄  ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██▀▀█▄  
░▒███▒█▄ ░██▓ ▒██▒░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░██▓ ▒██▒
░░ ▒▒░ ▒ ░ ▒▓ ░▒▓░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒░  ░   ░▒ ░ ▒░  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░
   ░   ░   ░░   ░ ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ 
    ░       ░           ░    ░  ░         ░    ░  ░   ░           ░  ░   ░        ░ ░     ░     
                                                                       ░                        


    
    ''')
banner()

urldata = input("Ingrese la url para generar el QR:")
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(f'{urldata}')

qrmake = qr.make_image(image_factory=StyledPilImage, module_drawer= RoundedModuleDrawer(), color_mask= VerticalGradiantColorMask(top_color=(18, 140, 126),bottom_color=(7, 94, 84)))
qrmake.save("QRgenerado.jpg")
print("QR GENERADO")
banner() 
