import sys

def main(): 
    lines()

def lines():
    try:
        with open(sys.argv[1], "r") as userfile: ##
            content = userfile.readlines()
            to_read = []
            for line in content:
                line = line.lstrip()
                to_read += line

            return
    except FileNotFoundError:
        sys.exit("File not found")
    except len(sys.argv) >= 2:
        sys.exit("Too many command-line arguments")
    except len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    
main()