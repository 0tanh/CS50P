fulltweet = input("gimme ur tweet hoe: ")
to_replace = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
for char in fulltweet:
    if char in to_replace:
        fulltweet = fulltweet.replace(char, "")
print("ur tweet without vowels: " + fulltweet)