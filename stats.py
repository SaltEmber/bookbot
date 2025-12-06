
def get_num_words(text):
    text = text.replace("\n", " ")
    words = text.split()
    return len(words)