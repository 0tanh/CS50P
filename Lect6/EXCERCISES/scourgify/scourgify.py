import csv
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too Few Command Line Arguments")
    
    if len(sys.argv) > 3:
        sys.exit("Too Many Command Line arguments")
    
    try:
        ##opens a reading csv as before and a writing csv as after
        with open(sys.argv[1], "r", encoding='utf-8') as Before, open(
            sys.argv[2] ,"w", encoding= 'utf-8') as After: 
            
            reader = csv.DictReader(Before) #makes a reader object for before
            
            new_fieldnames = ['first','last','house'] #outlines the new fieldnames for the writer
            writer = csv.DictWriter(After, fieldnames=new_fieldnames) #makes a writer object
            writer.writeheader() #writes header
            
            for row in reader:
                new_row = {} #creates new row variable to store to
                Cleaned_Name = row["name"].split(", ") #splits name from before
                new_row["first"] = Cleaned_Name[1] #makes the first row
                new_row["last"] = Cleaned_Name[0] #makes the last row
                new_row["house"] = row.get('house', '') #makes the house row
                writer.writerow(new_row) #writes the title row to the writer csv
            
    except FileNotFoundError: #error handling for before csv
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()