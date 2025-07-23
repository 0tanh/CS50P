from PIL import Image

def main():
    with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format)
        print(img.rotate(180, expand= 10))
        img.save("out.jpeg")

main()