def repeat_me(func):

    def wrapper(string, count):
        for i in range(count):
            func(string)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=3)
