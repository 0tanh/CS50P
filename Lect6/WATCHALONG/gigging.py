import csv

gigs = []

with open("gigs.csv") as file:
    for line in file:
        Venue, Person, Associated = line.rstrip().split(",")
        gig = {"Venue": Venue, "Person": Person, "Associated": Associated }
        gigs.append(gig)

for gig in gigs:
    print(f"{gig['Venue']} is associated with {gig['Person']} who I know from {gig['Associated']}")
    