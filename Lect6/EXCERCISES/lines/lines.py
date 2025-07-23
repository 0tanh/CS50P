import sys

def main(): 
    print(lines())

def lines():
    try:
        if len(sys.argv) >= 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        extension_test = sys.argv[1].split(".")
        if extension_test[1] != "py":
            sys.exit("Not a Python File")
        with open(sys.argv[1], "w") as userfile:
            content = userfile.readlines()
            LOC = 0
            for line in content:
                line = line.lstrip
                if line[0] == "#":
                    continue
                else:
                    LOC += 1
            print(LOC)
    except FileNotFoundError:
        sys.exit("File not found")

    
main()