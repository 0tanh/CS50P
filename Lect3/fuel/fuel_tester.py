def fuel():
    while True: #establishes loop
        try: #attempts the math
            User_Fraction = input("Fraction: ") #takes in input
            intergers = User_Fraction.split("/") #splits input into a list
            x = int(intergers[0]) #makes index 0 into actual interger from list
            y = int(intergers[1]) #makes index 1 into actual interger from list
            if x == 0: #checks if 0'd out so math doesn't break
                print("E")
            if x > y:
                raise Exception
            if ((x/y)*100) >= 99: #checks if full
                print("F")
            elif((x/y)*100) <= 1: #checks if empty
                print ("E")
            else:
                print(f"{round((x/y)*100)}%") #f string for ratio into percentage. built-in rounding
        except ZeroDivisionError: #exception for if division by 0
            print("Invalid Input: Zero Division Error (fuel tank amount set to 0)")
        except ValueError: #exception for if ValueError
            print ("Invalid Input: Value Error(please format fraction as 'x/y')")
        except Exception:
            print("Invalid Input")    
        else:
            break
    return

fuel()