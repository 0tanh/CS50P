import sys

extension_test = sys.argv[1].split(".")
if extension_test[1] != "py":
    sys.exit("Not a Python File")

else:
    print("it's a python AHHH")

