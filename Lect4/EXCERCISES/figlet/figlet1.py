from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))

elif len(sys.argv) == 3:
    if str(sys.argv[1]) not in ["-f", "--font"]:
        sys.exit("Invalid Usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")
    figlet.setFont(font = sys.argv[2])
    
txt = input("Input: ")

print(f"Output: \n {figlet.renderText(txt)}")
