import csv

gigs = []

with open("gigs.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        gigs.append(
            {"Venue": row["Venue"], 
             "Person":row ["Person"], 
             "Associated": row["Associated"]
             })

for gig in sorted(
    gigs, key=lambda gig: gig["Associated"]):
    print(f"{gig['Venue']} is associated with {gig['Person']} who I know from {gig['Associated']}")
    