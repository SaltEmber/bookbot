from io import FileIO
import sys

def main():
    path_to_file = "/home/salt/workspace/github.com/SaltEmber/bookbot/books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{count_words(file_contents)} words found in the document")

    mapped_letters = map_letters(file_contents)
    chars = []
    for entry, value in mapped_letters.items():
        chars.append({"char": entry, "num": value})
    chars.sort(reverse=True, key=sort_on)

    for part in chars:
        print(f"The '{part["char"]}' character was found {part["num"]} times")

def sort_on(dict):
    return dict["num"]

def count_words(file_contents):
    file_contents.replace('\n', "")
    components = file_contents.split(' ')
    length = 0
    for component in components:
        words = component.split('\n')
        for word in words:
            if not word == '':
                length += 1
    return length

def  map_letters(file_contents):
    map = {}
    file_contents = file_contents.lower()

    for element in file_contents:
        for char in element:
            if char.isalpha():
                try:
                    map[char] += 1
                except:
                    map[char] = 1
    return map
if __name__ == '__main__':
    main()
