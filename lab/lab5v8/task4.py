from PIL import Image, ImageDraw,ImageFont
image = Image.open('CAR.jpg')
image.show()

l = image.width * 0.45
v = image.height * 0.4
p = image.width * 0.8
n = image.height * 0.8
image = image.crop((l, v, p, n))

image = image.convert('L')

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 70)
draw.text((15, 210), "GOOD LUCK", fill="white", font=font)
image.show()
image.save("CAR_1.JPG", "JPEG")

image = image.resize((image.width // 2, image.height // 2)) # ш в
image.show()
image.save("CAR_2.JPG", "JPEG")


