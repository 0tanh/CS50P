accepted_coins = (50, 25, 10, 5)
Price = 50
Amount_due = int("")
while Amount_due > 0:
    # Check if the inserted coin is valid
    inserted_coin = int(input("Put your coin in here. NOTE! only 25, 10, or 5 cents accepted: "))
    if inserted_coin in accepted_coins:
        Amount_due -= inserted_coin
        print(f"Amount Due: {Amount_due}")
    else:
        print("Invalid coin")
        print(f"Amount Due: {Amount_due}")
        # If it is valid, calculate the remainder
        
if Amount_due == 0:
         print("Thank you for your purchase!")