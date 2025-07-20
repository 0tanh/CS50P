import csv

Venue = input("Where did you play? ")
Person = input("Who did you talk to to play? ")
Associated = input("How do you know them? ")

with open("gigging2.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=("Venue","Name",""))
    writer.writerow({Venue, Person, Associated})

