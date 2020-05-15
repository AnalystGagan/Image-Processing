from PIL import Image, ImageFilter

img = Image.open("./pokidex/pikachu.jpg")
filtered_img = img.convert('L')

invert = filtered_img.rotate(180)
invert.save('invert.png','png')

# filtered_img.save("grey.png",'png')
# filtered_img.show()