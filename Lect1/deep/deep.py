answer = input(str("What is the answer to life, the universe, and everything? "))
i = answer.lower()
# print(i)
if i == "42":
    print("true")
elif i.__contains__("forty two") or i.__contains__("forty-two"):
    print("true")
else:
    print("false")