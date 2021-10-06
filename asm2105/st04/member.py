from abc import abstractmethod, ABCMeta

from asm2105.st04.console import Input, Output


class Member(metaclass=ABCMeta):
    name: str = ''
    second_name: str = ''
    stipend: int = 0

    @abstractmethod
    def setData(self):
        self.name = Input('Имя: ', )
        self.second_name = Input("Фамилия: ", )

    @abstractmethod
    def showData(self):
        Output(self)

    @abstractmethod
    def __str__(self):
        return '{} {}, стипендия {}'.format(self.name, self.second_name, self.stipend)
