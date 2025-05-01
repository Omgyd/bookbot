from stats import count_book_words
from stats import num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_book_words(book)
    print(f"{count} words found in the document")
    print(num_characters(book))

main()