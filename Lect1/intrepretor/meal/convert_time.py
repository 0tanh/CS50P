def main(): 
    convert((input("Enter time in HH:MM format: "))) 


def convert(time):
    ## convert time to list
    time_parts = time.split(":")
    ## convert time to float
    float_time = float(int(time_parts[0])) + float(int(time_parts[1])/60)
    return float_time

main()