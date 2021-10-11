from abc import ABC, abstractmethod

class BaseInteractive(ABC):
    @abstractmethod
    def Enter(self, obj):
        pass

    @abstractmethod
    def Print(self, obj):
        pass


class ConsoleInteractive(BaseInteractive):
    def Enter(self, obj):
        for key in obj.__dict__.keys():
            if key!= 'id' and key != "interactive":
                obj.__dict__[key] = input(f'Введите {key}\n')

    def Print(self, obj):
        if obj.__str__ is not object.__str__:
            print(str(obj))
        else:
            for key, value in obj.__dict__.items():
                if key != "interactive":
                    print(key, ': ', value)