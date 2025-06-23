def main():
    snakecaser(input("enter a CamelCase string to turn it into a snake_case string: "))

def snakecaser(camel_case_string):
    snakecase =""
    for c in camel_case_string:
        if c.isupper():
            snakecase += "_" + c.lower()
        else:
            snakecase += c
    print(snakecase[1:])  # Remove the leading underscore

main()