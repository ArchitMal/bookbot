from stats import get_book_text
from stats import character_counter
from stats import sorter
from stats import sort_on
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    number_of_words = get_book_text(book_path)
    char_count = character_counter(book_path)
    final = sorter(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for character in final:
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()