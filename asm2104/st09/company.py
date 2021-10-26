from .file_strategy import FileStrategy
from .console_strategy import ConsoleStrategy


class Company:
    __array = []

    def __init__(self, array):
        self.__array = array

    def clearAllElements(self):
        self.__array.clear()

    # консоль
    def addElements(self):
        self.__array.extend(ConsoleStrategy.load())

    def printElements(self):
        ConsoleStrategy.dump(self.__array)

    # файл
    def loadElements(self):
        # из файла
        self.__array = FileStrategy.load()

    def saveElements(self):
        FileStrategy.dump(self.__array)
