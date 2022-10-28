import qrcode
import csv
from PIL import Image, ImageFont, ImageDraw 

title_font = ImageFont.truetype('arial.ttf', 15)

with open("./qr_data.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=';')
  for row in csvreader:
    #Se obtiene la cedula y se guarda en la lista
    data_cedula = row[0]
    data_nombre = row[1]
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=15,
            border=5)
    qr.add_data(data_cedula)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    imagen_name="./qr_litoplas/"+data_cedula+".png"
    img.save(imagen_name)
    #Agregar texto a la imagen
    my_image = Image.open(imagen_name)
    title_text = data_nombre
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50,15),title_text,font=title_font,align="center")    
    imagen_nombreqr="./qr_litoplas_nombres/"+data_nombre+".png"
    my_image.save(imagen_nombreqr)  

