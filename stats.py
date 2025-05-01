def count_book_words(book):
    return len(book.split())


def num_characters(book):
    char_dict = {}
    for char in book:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict