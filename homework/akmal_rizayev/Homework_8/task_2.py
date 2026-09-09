import sys

sys.set_int_max_str_digits(100000)


def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def show_num(gener, k):
    count = 0
    for number in gener:
        if count == k:
            print(number)
            break
        if k >= 0:
            count += 1
        else:
            print('Ошибка')
            break


show_num(fib(), 5)
show_num(fib(), 200)
show_num(fib(), 1000)
show_num(fib(), 100_000)
