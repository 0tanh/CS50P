def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if plate.isalnum():
        if 2 <= len(plate) <= 6:
            if plate[0].isalpha() and plate[1].isalpha():
                
                return True      
    else:
        return False

main()