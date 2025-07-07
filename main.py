from stats import (
    get_word_count,
    get_book_text,
    get_char_count,
    get_sorted_stats,
)
import sys


def main():
    # Check to make sure user passed in argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = "./" + sys.argv[1]
    short_file = file[2:]
    word_count = get_word_count(file)
    char_count = get_char_count(get_book_text(file))
    sorted_char_count = get_sorted_stats(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {short_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()
