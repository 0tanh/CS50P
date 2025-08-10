import sys
import os
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