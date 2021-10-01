"""
Файл  стратегий ввода вывода
"""
from abc import ABC, abstractmethod
from typing import List
from person import Student, MainStudent


class StrategyIO(ABC):
    @abstractmethod
    def enter(self, person: Student):
        pass

    def output(self, data: List):
        pass


class InputOutPutConsole(StrategyIO):
    def enter(self, person: Student):
        for key, val in person.__dict__.items():
            if key != 'is_main':
                person.__dict__[key] = input(f"{ key }: ")

    def output(self, data: List):
        print('-------Участники группы----------')
        for person in data:
            for key, val in person.__dict__.items():
                print(f"{key} : {val}")
            print("\n")
        print('---------------------------------')
