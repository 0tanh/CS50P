def main():
    monthsdict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    
    while True:
        try:
            userdate = input("Date: ")
            if "/" in userdate:
                list_userdate = userdate.split("/")
                month = int(list_userdate[0])
                day = int(list_userdate[1])
                year = int(list_userdate[2])
                if month > 12:
                    raise Exception
                elif day > 31:
                    raise Exception
                else:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            elif " " in userdate:
                list_userdate = userdate.replace(",", "").split(" ")
                day = int(list_userdate[1])
                if day > 31:
                    raise Exception
                year = int(list_userdate[2])
                if list_userdate[0] in monthsdict:
                    month = monthsdict[list_userdate[0]]
                    print(f"{year}-{month:02}-{day:02}")
                    break
            else:
                continue
            
        except (KeyError, ValueError, IndexError):
            print("Invalid Date format.")
            continue
        except Exception:
            print("Invalid Date format.")
            continue

main()