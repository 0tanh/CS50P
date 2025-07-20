namelist = []

with open("names2.txt") as file:
    for line in file:
        namelist.append(line.rstrip())
        
for name in sorted(namelist):
    print(f"hello, {name}")