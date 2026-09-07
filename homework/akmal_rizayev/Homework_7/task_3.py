from os.path import split

result_strings = '''результат операции: 42
результат операции: 54
результат работы программы: 209
результат: 2'''

def get_numbers_and_add(new_str):
    words_in_str = new_str.split()
    for word in words_in_str:
        if word.isnumeric():
            print(int(word) + 10)

get_numbers_and_add(result_strings)
