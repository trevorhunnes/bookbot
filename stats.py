# Accept a file path and return text from that file as a string
def get_book_text(file):
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()

    return file_contents


# Accept a file path and return word count as int
def get_word_count(file):
    words = get_book_text(file).split()
    count = 0
    for word in words:
        count += 1

    return count


# Accept string and return a dictionary with character->count
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


def sort_on(items):
    return items["num"]


# Accept a dictionary(character->count) and return of list of dictionaries
# Sort dictionaries from largest count to smallest
def get_sorted_stats(chars):
    sorted_chars = []
    for char in chars:
        if char.isalpha():
            sorted_chars.append({"char": char, "num": chars[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
