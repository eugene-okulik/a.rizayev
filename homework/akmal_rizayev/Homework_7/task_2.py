words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def print_words(dictionary):
    for word, repeats in dictionary.items():
        print(word * repeats)


print_words(words)
