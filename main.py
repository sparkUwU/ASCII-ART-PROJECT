from PIL import Image
import os

chars = "@%#*+=-:. "

print("python is looking in: ")
print(os.getcwd())

filename = input("Enter the image filename: ")

try:
    image = Image.open(filename)
except FileNotFoundError:
    print("File Not Found!!!")
    exit()
except Exception:
    print("That isn't a valid image.")
    exit()

gray_image = image.convert("L")
gray_image.save("gray.jpg")

new_width = 100
new_height = int(gray_image.height * new_width / gray_image.width * 0.5)
gray_image = gray_image.resize((new_width, new_height))


for y in range(gray_image.height):
    for x in range(gray_image.width):
        pixel = gray_image.getpixel((x,y))

        index = pixel * len(chars) // 256

        print(chars[index], end="")

    print()