from PIL import Image
import os

print("python is looking in: ")
print(os.getcwd())


def load_image(filename):
    try:
        image = Image.open(filename)
        return image
    except FileNotFoundError:
        print("File Not Found!!!")
        exit()
    except Exception:
        print("That isn't a valid image.")
        exit()


def get_width():
    while True:
        try:
            width = int(input("Enter ASCII width: "))
            if width <= 0:
                print("Width must be greater than 0.")
                continue

            return width
            
        except ValueError:
            print("Please enter a number.")



def convert_to_ascii(image, width):

    chars = "@%#*+=-:. "

    gray_image = image.convert("L")

    new_height = int(gray_image.height * width / gray_image.width * 0.5)
    gray_image = gray_image.resize((width, new_height))

    ascii_art = ""

    for y in range(gray_image.height):
        for x in range(gray_image.width):
            pixel = gray_image.getpixel((x,y))

            index = pixel * len(chars) // 256

            ascii_art += chars[index]

        ascii_art += "\n"

    return ascii_art



def save_ascii(ascii_art, filename):
    with open(filename, "w") as file:
        file.write(ascii_art)



def main():

    filename = input("Enter the image filename: ")
    image = load_image(filename)
    width = get_width()

    ascii_art = convert_to_ascii(image, width)
    print(ascii_art)

    save_ascii(ascii_art, "ascii_art.txt")
    print("ASCII art saved to ascii_art.txt")


if __name__=="__main__":
    main()