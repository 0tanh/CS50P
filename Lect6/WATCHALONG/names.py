import csv

with open("gigs.csv") as file:
    for line in file:
        Venue, person, associated = line.rstrip().split(",")
        # row = row [1:]
        print(f"{Venue} is associated with {person} who I know from {associated}")
    