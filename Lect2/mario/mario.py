def main():
    print_square(2)
    print_column(5)
    print_row(6)

##print square brick
def print_square(size):
    for i in range(size):
        print("#" * size, sep ="." , end=" \n")

def print_column(size):
    for _ in range(size):
        print("#", sep =".", end=" \n")

def print_row(size):
    print("#"* size, sep ="", )

main()

