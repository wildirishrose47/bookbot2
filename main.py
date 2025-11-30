import sys

from stats import num_characters, num_words, sorted_chars


def main():
    if len(sys.argv) == 2:
        path_to_book = sys.argv[1]
        text = get_book_text(path_to_book)
        word_count = num_words(text)
        sorted = sorted_chars(num_characters(text))
        pretty_print(path_to_book, word_count, sorted)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(book):
    with open(book) as f:
        return f.read()


def pretty_print(path, count, sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for key in sort:
        print(f"{key['char']}: {key['num']}")


main()
