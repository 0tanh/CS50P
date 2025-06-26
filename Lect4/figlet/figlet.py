import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
figlet_list =figlet.getFonts()

if len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    input("") 
elif sys.argv[2] in figlet_list:
    figlet.setFont(font=f)
    input("")



# if:
#     

# elif:
#     sys.exit('Invalid usage')