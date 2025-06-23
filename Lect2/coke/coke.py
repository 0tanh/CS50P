def main():
    accepted_coins = (50, 25, 10, 5)
    amount_Due = 50
    inserted_coin = int(input("Put your coin in here. NOTE! only 25, 10, or 5 cents accepted: "))
    remainder = amount_Due - inserted_coin
    # while remainder >= amount_Due:
    #     print(f"Amount Due: {remainder}")   
    def coke_machine (inserted_ coin, amount_Due, accepted_coins)
        accepted_coins = (50, 25, 10, 5)
        amount_Due = 50
        remainder = amount_Due - inserted_coin
        while remainder > 0:
            # Check if the inserted coin is valid
            if inserted_coin not in accepted_coins:
                print("Invalid coin")
                print(f"Amount Due: {amount_Due}")
                return amount_Due
            # If it is valid, calculate the remainder
            if inserted_coin in accepted_coins:
                    print(f"Amount Due: {remainder}")
                    inserted_coin = int(input("Put your next coin in here. NOTE! only 25, 10, or 5 cents accepted: "))
                    return remainder
            if remainder == 0:
                    print("Thank you for your purchase!")
                    return 0
    coke_machine(inserted_coin, 50, accepted_coins) 
        
               
main()