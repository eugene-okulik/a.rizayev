old_string = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
              "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

string_list = old_string.split(" ")
new_string_list = []

for word in string_list:
    if ',' in word:
        new_word = word[:-1] + 'ing' + ','
    elif '.' in word:
        new_word = word[:-1] + 'ing' + '.'
    else:
        new_word = word + 'ing'
    new_string_list.append(new_word)

new_string = ' '.join(new_string_list)
print(new_string)
