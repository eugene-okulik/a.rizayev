def calc_dec(func):

    def wrapper(fir, sec):
        if fir >= 0 and sec >= 0:
            if fir == sec:
                result = func(fir, sec, '+')
            elif fir > sec:
                result = func(fir, sec, '-')
            elif sec > fir:
                result = func(fir, sec, '/')
            else:
                return
        else:
            result = func(fir, sec, '*')
        print(result)

    return wrapper

@calc_dec
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        raise ValueError


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

calc(a, b)
