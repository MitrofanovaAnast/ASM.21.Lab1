from abc import ABC, abstractmethod

class BaseInteraction(ABC):
    def __init__(self, obj):
        self.obj=obj

    @abstractmethod
    def Out(self):
        pass

    @abstractmethod
    def In(self):
        pass

class ConsoleInteraction(BaseInteraction):
    def Out(self):
        if self.obj.__str__ is not object.__str__:
            print(str(self.obj))
        else:
            for key, value in self.obj.__dict__.items():
                if key != "strategy":
                    print(key, ': ', value)


    def In(self):
        for key in self.obj.__dict__.keys():
            if key!= 'id' and key != "strategy":
                self.obj.__dict__[key] = input(f'Введите {key}\n')