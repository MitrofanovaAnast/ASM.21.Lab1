from asm2104.st09.file_strategy import FileStrategy
from asm2104.st09.console_strategy import ConsoleStrategy


class Company:
    __array = []
    __strategy = ConsoleStrategy

    def __init__(self, array):
        self.__array = array

    def chooseStrategy(self):
        menu = [
            {'label': 'Консоль', 'strategy': ConsoleStrategy},
            {'label': 'Файл', 'strategy': FileStrategy}
        ]
        for i in range(len(menu)):
            print('{0} - {1}'.format(i, menu[i]['label']))

        self.__strategy = menu[int(input())]['strategy']

    def clearAllElements(self):
        self.__array.clear()

    def setElements(self):
        self.__array.extend(self.__strategy.load())

    def getElements(self):
        self.__strategy.dump(self.__array)
