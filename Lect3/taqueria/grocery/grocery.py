groceries = {
    }

try:
    while True:
        item = (input().upper())
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
except EOFError:
    for item in groceries:
        print(f"{groceries[item]} {item}")