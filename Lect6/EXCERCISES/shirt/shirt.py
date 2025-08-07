import PIL
import os
import sys

def main():
    #error handling for command line arguments
    if len(sys.argv) == 1:
        sys.exit("Too Few Command Line Arguments")
    
    if len(sys.argv) > 3:
        sys.exit("Too Many Command Line arguments")
    
    #defines a bunch of variables
    formats = [".jpeg",".jpg",".png"]
    image_in = sys.argv[1] 
    image_out = sys.argv[2]
    extension_in = os.path.splitext(image_in)[1] 
    extension_out = os.path.splitext(image_out)[1]
    
    #error handling for extensions
    if extension_in or extension_out not in formats:
        sys.exit("Not An Acceptable Image Format. Please use .jpeg, .jpg or .png")
    if extension_in != extension_out:
        sys.exit("Input and output have different extensions")
      
    try:
        shirt = PIL.Image.open("shirt.png")
        size = shirt.size
        PIL.photo.paste(shirt, shirt)
    except FileNotFoundError:
        sys.exit("Input does Not Exist")

if __name__ =="__main__":
    main()
