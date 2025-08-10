import PIL
import os
import sys

def main():
    #error handling for command line arguments
    if len(sys.argv) == 1:
        sys.exit("Too Few Command Line Arguments")
    
    if len(sys.argv) > 4:
        sys.exit("Too Many Command Line arguments")
    
    #defines a bunch of variables
    formats = [".jpeg",".jpg",".png"]
    overlay = sys.argv[1]
    base_image = sys.argv[2] 
    image_out = sys.argv[3]
    extension = ()
    extension += os.path.splitext(overlay)[1], os.path.splitext(base_image)[1], os.path.splitext(image_out)[1]
    check = set(extension)

    #error handling for extensions
    if not check.issubset(formats):
        print("Not An Acceptable Image Format. Please use .jpeg, .jpg or .png")
    if len(check) > 1:
        print("Input and output have different extensions")
      
    try:
        shirt = PIL.Image.open(overlay)
        # size = shirt.size
        finalimage = base_image.paste(shirt, shirt)
        finalimage.save(image_out)
    
    except FileNotFoundError:
        sys.exit("Input does Not Exist")

if __name__ =="__main__":
    main()

"""
input: 2 pictures (pic 1, pic 2)
output: 1 picture (pic 3)

process:
check if picture x 2
 - exists
 - is picture
 -

check if pic
    |
    |
no -- yes   
|       |
        change size

if picture (yes)
- check for size format
- get size

if picture (no)
= error handling

change size
length * width
pic 1 size must equal pic 2 size

combine pics
put pic 1 on pic 2
gives pic 3 aka output


"""
