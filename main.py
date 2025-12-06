from stats import get_num_words, get_num_letters, sorting_num_letters

def get_book_text(filepath):
    with open(filepath, encoding="utf-8-sig") as f:
        return f.read()

def main():
    file_location = "books/frankenstein.txt"

    file_contents = get_book_text(file_location)
    #print(file_contents)

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {file_location}...")

    print("----------- Word Count ----------")
    
    num_words = get_num_words(file_contents)
    print(f'Found {num_words} total words')

    print("--------- Character Count -------")
    letters = get_num_letters(file_contents)

    letters = sorting_num_letters(letters)
    for letter in letters:
        print(f"{letter['letter']}: {letter['num']}")

    print("============= END ===============")
main()