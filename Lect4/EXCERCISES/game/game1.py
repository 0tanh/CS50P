import random
while True:
    try:
        Level = int(input("Level: "))
        answer = random.randrange(1, Level)
        if Level <= 0:
            raise ValueError
        break
    except (TypeError, ValueError):
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess == answer:
            print("Just right!")
            break
        elif guess > answer:
            print("Too Big!")
        elif guess < answer:
            print("Too Small!")
    except (ValueError, TypeError):
        pass