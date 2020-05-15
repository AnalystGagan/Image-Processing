from PIL import Image, ImageFilter

img = Image.open("./original.jpg")
# reduce_img = img.resize((400,400))
'''
method thumbnail auto generates the 
correct aspect ratio within the range 
specified ex. (400,400)
'''
img.thumbnail((400,400)) 
img.save('by method thumbnail.jpg') 

# reduce_img.save('thubnail.png','png')


# filtered_img = img.convert('L')

# invert = filtered_img.rotate(180)
# invert.save('invert.png','png')