import csv
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too Few Command Line Arguments")
    
    if len(sys.argv) > 3:
        sys.exit("Too Many Command Line arguments")
    
    try:
        with open(sys.argv[1], "r", encoding='utf-8') as Before, open(
            sys.argv[2] ,"w", encoding= 'utf-8') as After:
            
            reader = csv.DictReader(Before)
            new_fieldnames = ['first','last','house']
            
            writer = csv.DictWriter(After, fieldnames=new_fieldnames)
            writer.writeheader()
            
            for row in reader:
                new_row = {}
                Cleaned_Name = row["name"].split(", ")
                new_row["first"] = Cleaned_Name[1] 
                new_row["last"] = Cleaned_Name[0]
                new_row["house"] = row.get('house', ''.strip())
                writer.writerow(new_row)
            
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()