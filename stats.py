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


def sort_on(d):
    return d["num"]

def sorted_dicts(dicts):
    sorted_list = []
    for ch in dicts:
        sorted_list.append({"char": ch, "num": dicts[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list