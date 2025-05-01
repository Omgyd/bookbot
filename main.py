from stats import count_book_words
from stats import num_characters
from stats import sorted_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, chars_sorted_list):
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = count_book_words(text)
        chars_dict = num_characters(text)
        chars_sorted_list = sorted_dicts(chars_dict)

        print_report(book_path, num_words, chars_sorted_list)

main()