def Input(field):
    return input(field)


def Output(o):
    print(o)


def MenuInput(text=''):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print('Введите что-то адекватное')
