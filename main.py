def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return len(file_contents.split())

def main():
    print(get_book_text("./books/frankenstein.txt"))


if __name__ == "__main__":
    main()