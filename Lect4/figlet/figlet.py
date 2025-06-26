import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
figlet_list =figlet.getFonts()

if 0 < len(sys.argv()) < 2:
    sys.exit("Invalid usage")

if sys.argv[1] in figlet_list:




# if:
#     

# elif:
#     sys.exit('Invalid usage')