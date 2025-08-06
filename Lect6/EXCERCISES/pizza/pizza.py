import sys
import os
import csv
import tabulate

def main():
    if len(sys.argv) > 2: ##Error handling for bad user input
        sys.exit("Too Many Command Line Arguments")
    
    Menu = sys.argv[1] #make menu variable
    
    extension = os.path.splitext(Menu)[1] #error handling for not being a CSV
    if extension != ".csv":
      sys.exit("Not a CSV file")
    
    try:
        with open(Menu, "r", encoding="utf-8") as OnScreen: #opens CSV
            reader = csv.DictReader(OnScreen) #makes variable to input into tabulation
            print(tabulate(reader, tablefmt="grid"))

    ##except if File doesn't exist.
    except FileNotFoundError:
        sys.exit("File Does Not Exist")
    
main()