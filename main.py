from stats import get_word_count


def main():
    word_count = get_word_count("./books/frankenstein.txt")
    print(f"{word_count} words found in the document")


main()
