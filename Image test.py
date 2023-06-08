from PIL import Image

im = Image.open("ballimage.jpg")

print(im.size)

im = im.rotate(45)

print(im.size)

im.save("eiffel_tower_rotate_01.jpg")
im.show()
