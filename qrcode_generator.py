import qrcode

data = input("Enter here : ")

qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
qr.add_data(data)
 
qr.make(fit = True)

img = qr.make_image(fill_color = 'white',
                    back_color = 'black')
 
img.save('MyQRCode.png')

print("Qrcode Generated successfuly ")








