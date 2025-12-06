
def get_num_words(text):
    text = text.replace("\n", " ")
    words = text.split()
    return len(words)

def get_num_letters(text):
    text = text.replace("\n", "")

    counting_dict = {}
    for letter in text:
        if not letter.lower() in counting_dict.keys():
            counting_dict[letter.lower()] = 1
            continue
        counting_dict[letter.lower()] += 1
    
    return counting_dict
        