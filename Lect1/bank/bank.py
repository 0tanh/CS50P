def main():
    bank(input("Greet me: "))
def bank(str):
    if str=="hello":
        print("$0")
    if str[0] == ("h") or str[0] == ("H"):
        print("$20")
    else:
        print("$100")

main()