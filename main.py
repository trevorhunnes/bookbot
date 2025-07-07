from stats import (
    get_word_count,
    get_book_text,
    get_char_count,
    get_sorted_stats,
)


def main():
    file = "./books/frankenstein.txt"
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
