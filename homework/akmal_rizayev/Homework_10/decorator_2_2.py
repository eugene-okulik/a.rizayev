def repeat_me(count):

    def inner(func):

        def wrapper(string):
            for i in range(count):
                func(string)

        return wrapper

    return inner


@repeat_me(count=3)
def example(text):
    print(text)


example('print me')
