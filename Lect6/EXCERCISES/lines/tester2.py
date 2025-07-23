with open("lines.py", "r") as userfile:
    contentz = userfile.readlines()
    print(contentz)
    LOC = 0
    for line0c0de in contentz:
        line0c0de = line0c0de.lstrip()
        if line0c0de[0] == "#":
            continue
        else:
            LOC += 1
    print(LOC)