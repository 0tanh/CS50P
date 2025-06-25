distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    
    while True:
        try:
            au = (float((distances[spacecraft])))
            m = convert(au)
            print(f"{spacecraft} is {m} m away")
            break
        except ValueError:
            print(f"'{distances[spacecraft]}' is formatted incorrectly and cannot be converted")
            spacecraft = input("Enter a spacecraft: ")
            
        except KeyError:
            print(f"'{spacecraft}' is not in our database")
            spacecraft = input("Enter a spacecraft: ")
            
    
    


def convert(au):
    return au * 149597870700


main()
