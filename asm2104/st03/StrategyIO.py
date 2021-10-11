from abc import ABC, abstractmethod
from asm2104.st03.student import Student
from typing import List

class StrategyIO(ABC):
    @abstractmethod
    def enter(self, person: Student):
        pass

    def printout(self, data: List):
        pass

class ConsoleIO(StrategyIO):
    def enter(self, person: Student):
        for key, val in person.__dict__.items():
            if key != 'is_VUC':
                person.__dict__[key] = input(f"{ key }: ")

    def printout(self, data: List):
        for person in data:
            for key, val in person.__dict__.items():
                print(f"{key} : {val}")