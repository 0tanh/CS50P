def main():
    print(value(input("Greet me: ")))

def value(greeting):
    if greeting=="hello":
        return ("$0")
    elif greeting[0] == ("h") or greeting[0] == ("H"):
        return ("$20")
    else:
        return ("$100")

if __name__ == "__main__":
    main()