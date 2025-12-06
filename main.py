def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    text = text.replace("\n", " ")
    words = text.split()
    return len(words)

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(file_contents)

    num_words = count_words(file_contents)
    print(f'Found {num_words} total words')
main()