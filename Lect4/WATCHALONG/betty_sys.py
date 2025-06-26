import sys

if len(sys.argv) < 2:
    sys.exit("not enough arguments")
    

for arg in sys.argv[1:5]:
    print(arg)