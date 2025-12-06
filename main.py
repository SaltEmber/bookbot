from stats import get_num_words, get_num_letters

def get_book_text(filepath):
    with open(filepath, encoding="utf-8-sig") as f:
        return f.read()

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(file_contents)

    num_words = get_num_words(file_contents)
    print(f'Found {num_words} total words')

    letters = get_num_letters(file_contents)
    print(letters)
main()