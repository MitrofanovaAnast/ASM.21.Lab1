from .fc import FC
from .fileIO import FileIO
from .consoleIO import ConsoleIO


FC = FC()


def chooseStrategy():
    menu = [
        {'label': 'Консоль', 'strategy': ConsoleIO},
        {'label': 'Файл', 'strategy': FileIO}
    ]
    for i in range(len(menu)):
        print('{0} - {1}'.format(i, menu[i]['label']))

    return menu[int(input())]['strategy']


def writeElems():
    FC.write(chooseStrategy())


def readElems():
    FC.read(chooseStrategy())


def main():
    menu = [
        {'label': 'Добавить элементы', 'handler': writeElems},
        {'label': 'Вывести список элементов', 'handler': readElems},
        {'label': 'Очистить все', 'handler': FC.clearAll},
    ]

    while True:
        print()
        for i in range(len(menu)):
            print('{0} - {1}'.format(i, menu[i]['label']))
        menu[int(input())]['handler']()


if __name__ == '__main__':
    main()
