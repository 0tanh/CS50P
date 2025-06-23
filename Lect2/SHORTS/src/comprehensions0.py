from helpers import get_words, save_counts


def main():
    counts = {}
    words = get_words("address.txt")
    lowercase_words = [word.lower() for words in words]

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)


main()
