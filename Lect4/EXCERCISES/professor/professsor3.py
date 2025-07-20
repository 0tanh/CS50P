import random


def main():
    level = get_level()
    games = 0
    points = 0
    while games < 10:
        games += 1
        x, y = generate_integer(level)
        tries = 0
        while True:
            answer = x + y
            if tries == 3:
                print(f"{x} + {y} = {answer}")
                break
            else:
                try:
                    useranswer = int(input(f"{x} + {y} = "))
                    if useranswer == answer:
                        points += 1
                        break
                    else:
                        tries +=1
                        print("EEE")
                        pass
                except (ValueError, TypeError):
                    print("EEE")
                    pass

    print(f"You won {points}/{games} games!")
   


def get_level():
    while True:
        try:
            Level = int(input("Level: "))
            if Level not in [1,2,3]:
                raise ValueError
            return Level
        except (ValueError, TypeError):
            pass
        


def generate_integer(level):
    # selects difficulty
    if level == 1:
        x = random.randint(0, 5)
        y = random.randint(0, 5)
    elif level == 2:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
    elif level == 3:
        x = random.randint(0, 20)
        y = random.randint(0, 20)
    return x, y

if __name__ == "__main__":
    main()