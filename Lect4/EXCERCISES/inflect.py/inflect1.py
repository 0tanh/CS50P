import inflect
p = inflect.engine()
Names = []
while True:
    try:
        Names.append(input("Name: "))  
    except EOFError:
        print(p.join(Names))
        break