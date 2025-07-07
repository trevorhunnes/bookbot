def get_book_text(file):
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()

    return file_contents


def get_word_count(file):
    words = get_book_text(file).split()
    count = 0
    for word in words:
        count += 1

    return count


def get_char_count(text):
    char_count = {}
    text = text.lower()
    chars = list(text)
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
