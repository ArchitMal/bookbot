from stats import get_book_text

def main():
    number_of_words = get_book_text("./books/frankenstein.txt")
    print(f"{number_of_words} words found in the document")


if __name__ == "__main__":
    main()