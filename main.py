from stats import get_word_count
from stats import get_book_text
from stats import get_char_count


def main():
    word_count = get_word_count("./books/frankenstein.txt")
    char_count = get_char_count(get_book_text("./books/frankenstein.txt"))
    print(f"{word_count} words found in the document")
    print(char_count)


main()
