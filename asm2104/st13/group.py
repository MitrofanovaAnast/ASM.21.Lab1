import pickle

from asm2104.st13.ConsoleIO import ConsoleIO
from asm2104.st13.fileIO import FileIO
from asm2104.st13.headman import Headman
from asm2104.st13.student import Student

elementTypes = [
    {'text': 'Добавить старосту', 'class': Headman},
    {'text': 'Добавить обычного студента', 'class': Student}
]

classes = [
    {'text': 'Файл', 'class': FileIO},
    {'text': 'Консоль', 'class': ConsoleIO}
]

class Group:
    def __init__(self, strategy, list=[]):
        self.list = list
        self.strategy = strategy

    def addElement(self):
        for i in range(len(elementTypes)):
            print('{0}. {1}'.format(i, elementTypes[i]['text']))
        element = int(input())
        self.list.append(elementTypes[element]['class']())

    def clearList(self):
        self.list.clear()

    def __changeStrategy(self):
        print('Выберите вывод')
        for i in range(len(classes)):
            print('{0}. {1}'.format(i, classes[i]['text']))
        element = int(input())
        self.strategy = classes[element]['class']

    def dump(self):
        self.__changeStrategy()
        self.strategy.dump(self.list)

    def load(self):
        self.__changeStrategy()
        self.list = self.strategy.load()
