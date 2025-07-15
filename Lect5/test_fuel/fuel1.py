def main():
    # User_Fraction = input("Fraction: ")
    # print(gauge(Convert(User_Fraction)))
    
def Convert(fraction):
    while True:
        try:
            intergers = fraction.split("/")
            x = int(intergers[0])
            y = int(intergers[1])
            percentage = ((x/y)*100)
            if x == 0: #checks if 0'd out so math doesn't break
                return("E")
            if x <= 0:
                raise ValueError
            if x > y:
                raise ValueError
            if percentage > 100:
                raise ValueError
            return percentage
        except ZeroDivisionError:
            raise ZeroDivisionError
        except ValueError:
            raise ValueError
        except TypeError:
            raise TypeError
        except Exception:
            raise Exception


def gauge(percentage):
    try:
        if percentage == "E":
            return ("E")
        elif percentage >= 99: #checks if full
            return ("F")
        elif percentage <= 1: #checks if empty
            return ("E")
        else:
            return f"{round(percentage)}%" #f string for ratio into percentage. built-in rounding
    except ZeroDivisionError: #exception for if division by 0
        raise ZeroDivisionError
    except ValueError: #exception for if ValueError
        raise ValueError

if __name__ == "__main__":        
    main()

main()