def main(): 
    
    meal_check(convert((input("Enter time in HH:MM format: ")))) 


def convert(time):
    ## convert time to list
    time_parts = time.split(":")
    ## convert time to float
    float_time = float(int(time_parts[0])) + float(int(time_parts[1])/60)
    return float_time
     
    
def meal_check(float_time):
    ## check if time is in meal time
    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")
    else:
        print("not meal time")  

# if __name__ == "__main__":
main()