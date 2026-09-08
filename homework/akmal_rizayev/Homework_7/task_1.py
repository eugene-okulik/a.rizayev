new_number = 3

while True:
    input_num = int(input('Угадайте цифру: '))
    if input_num == new_number:
        print('Поздравляю! Вы угадали!')
        break
    print('попробуйте снова')
