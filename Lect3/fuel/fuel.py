def main():
    User_Fraction = input("Fraction: ")
    Fraction_Converter(User_Fraction)

    
def Fraction_Converter(str):
    try:
        intergers = str.split("/")
        x = intergers[0]
        y = intergers[1]
        percentage = print(f"{(x/y)*100}%")
        return percentage
    except ZeroDivisionError:
        print("Invalid Input")
        pass
    except TypeError:
        print("Invalid Input")
        pass

        
main()