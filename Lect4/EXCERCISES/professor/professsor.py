import random


def main():
    get_level()
    generate_integer
    points = 0
    ##problem chunk
    x = random.randint(0, 20)
    y = random.randint(0, 20)
    tries = 0
    while tries < 3:
        answer = x + y
        if tries < 3:
            try:
                useranswer = int(input(f"{x} + {y} = "))
                if useranswer == answer:
                    points += 1
                    break
                else:
                    tries +=1
                    pass
            except ValueError:
                pass
        else:
            print("EEE")
            break
   


def get_level():
    while True:
        try:
            Level = int(input("Level: "))
            if Level not in [1,2,3]:
                raise ValueError
            break
        except (ValueError, TypeError):
            pass


def generate_integer(level):
    x = random.randint(0, 20)
    y = random.randint(0, 20)
    return x and y

if __name__ == "__main__":
    main()