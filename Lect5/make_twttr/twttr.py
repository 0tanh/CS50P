##Refactored to be a function

# fulltweet = input("gimme ur tweet: ")
# to_replace = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
# for char in fulltweet:
#     if char in to_replace:
#         fulltweet = fulltweet.replace(char, "")
# print("ur tweet without vowels: " + fulltweet)

def main():
    word = input("gimme ur tweet hoe: ")
    print(shorten(word))


def shorten(word):
    to_replace = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    for char in word:
        if char in to_replace:
            word = word.replace(char, "")
    return f"ur tweet without vowels: {word}"

if __name__ == "__main__":
    main()