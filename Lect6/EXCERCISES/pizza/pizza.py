import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2: ##Error handling for bad user input
        sys.exit("Too Many Command Line Arguments")
    
    Menu = sys.argv[1] #make menu variable
    
    extension = os.path.splitext(Menu)[1] #error handling for not being a CSV using os.path.splittext method.
    if extension != ".csv":
      sys.exit("Not a CSV file")
    
    try:
        with open(Menu, "r", encoding="utf-8") as OnScreen: #opens CSV
            reader = csv.DictReader(OnScreen) #makes reader to read
            All_Items =[] #makes list variable for easier tabulisation
            for row in reader: #reads each row
                All_Items.append(row) 
            print(
                tabulate(All_Items, headers= "keys", tablefmt="grid")) #makes a table from it all
            
    except FileNotFoundError: ##except if File doesn't exist.
        sys.exit("File Does Not Exist")

main()