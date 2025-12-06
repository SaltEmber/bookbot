from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(file_contents)

    num_words = get_num_words(file_contents)
    print(f'Found {num_words} total words')
main()