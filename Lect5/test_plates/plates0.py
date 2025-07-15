def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Checks if alphanumeric
    if plate.isalnum():
        #Checks if length is allowed
        if 2 <= len(plate) <= 6:
            #Checks if first 2 characters are letters
            if plate[0].isalpha() and plate[1].isalpha():
                #Finds number finder as a boolean and then
                number_finder = False
                for char in plate:
                    if char.isdigit():
                        number_finder = True
                    #If the boolean is true and a letter is found afterwards
                    elif number_finder and char.isalpha():
                        return False
                #Checks to see if first digit is 0
                for char in plate:
                    if char.isdigit():
                        if char == '0':
                            return False
                        break        
                return True 
            else:
                return False
        else:
            return False     
    else:
        return False

if __name__ == "__main__":
    main()