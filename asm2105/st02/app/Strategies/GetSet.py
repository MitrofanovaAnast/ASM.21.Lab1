from abc import ABC, abstractmethod

class BaseGetSet(ABC):
    def __init__(self, obj):
        self.obj=obj

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def set(self):
        pass

class ConsoleGetSet(BaseGetSet):
    def print(self):
        for key, value in self.obj.__dict__.items():
            if key != "strategy":
                print(key,': ', value)

    def set(self):
        for key, value in self.obj.get_attribs().items():
            self.obj.__dict__[key] = input(value)

