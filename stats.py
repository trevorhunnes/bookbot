def get_word_count(file):
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1

    return count
