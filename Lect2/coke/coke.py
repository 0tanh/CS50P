def main():
    accepted_coins = (50, 25, 10, 5)
    amount_Due = 50
    # remainder = amount_Due - inserted_coin
    # while remainder >= amount_Due:
    #     print(f"Amount Due: {remainder}")   
    coke_machine(50, accepted_coins) 

        
def coke_machine (amount_Due, accepted_coins):
    # remainder = amount_Due - inserted_coin
    remainder = amount_Due
    
    while remainder > 0:
        inserted_coin = int(input("Put your coin in here. NOTE! only 25, 10, or 5 cents accepted: "))
        
        # Check if the inserted coin is valid
        if inserted_coin not in accepted_coins:
            print("Invalid coin")
            print(f"Amount Due: {amount_Due}")
            continue # Start loop again
        
        remainder = remainder - inserted_coin
        print(f"Amount Due: {remainder}")
        
        print("Thank you for your purchase!")
        # return remainder
        if remainder == 0:
            print("Thank you for your purchase!")
            return 0
         
main()

## Function syntax
# return - end of function
# exit - exits the function/program


## Loop syntax
# continue - start loop again
# break - exit loop