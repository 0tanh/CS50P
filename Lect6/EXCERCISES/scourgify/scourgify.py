import csv
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too Few Command Line Arguments")
    
    if len(sys.argv) > 4:
        sys.exit("Too Many Command Line arguments")
    
    try:
        with open(sys.argv[1], "r", encoding='utf-8') as Before, open(
            sys.argv[2] ,"w", encoding= 'utf-8') as After:
            reader = csv.DictReader(Before)
            writer = csv.DictWriter(After, fieldnames=reader.fieldnames[1] + ["first"] + ["last"])
            for row in reader:
                Cleaned_Name = row.split(",")
                row["first"] = Cleaned_Name[1] 
                row["last"] = Cleaned_Name[0]
            writer.writerow(row)
    
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

main()