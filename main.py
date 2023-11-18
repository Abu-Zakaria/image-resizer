from PIL import Image
import math

image = Image.open("sample.png", 'r')

width = image.size[0]
height = image.size[1]

resize_scale = float(input("Choose a resize scale: "))

new_width = width * resize_scale
new_height = height * resize_scale

new_size = (int(new_width), int(new_height))

new_image = Image.new(mode='RGB', size=new_size, color=0)

for i in range(int(new_height)):
    y_index = math.floor(int(i / resize_scale))

    for j in range(int(new_width)):
        # i = iteration for new image's width
        # resize_scale = 2x
        #     i / 2
        # >>> 0 / 2 = 0.0 -> floor -> 0
        # >>> 1 / 2 = 0.5 -> floor -> 0
        # >>> 2 / 2 = 1.0 -> floor -> 1
        # >>> 3 / 2 = 1.5 -> floor -> 1
        # >>> 4 / 2 = 2.0 -> floor -> 2
        # >>> 5 / 2 = 2.5 -> floor -> 2
        # ...

        x_index = math.floor(int(j / resize_scale))

        pixel = image.getpixel((x_index, y_index))

        new_image.putpixel((j, i), pixel)

try:
    new_image.save("new_image.jpg", format="JPEG")
    print("Successfully saved the image!")
except OSError:
    print("Couldn't save the image")


