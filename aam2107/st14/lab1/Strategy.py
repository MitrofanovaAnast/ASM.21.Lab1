from abc import ABC, abstractmethod
import pickle, shelve


class Strategy(ABC):

    @abstractmethod
    def outputinfo(self, obj) -> None:
        pass

    @abstractmethod
    def inputargument(self, obj, name_argument, argument) -> None:
        pass

class PickleStategy:
    def fileoutput(self, obj):
        pickle.dump(obj, open("data.dat", "wb"))

    def fileinput(self):
        obj = pickle.load(open("data.dat", "rb"))
        return obj


class ConsoleIO:
    def outputinfo(self, obj):
        for key, value in obj.__dict__.items():
            if key != "strategy":
                print(key, value)

    def inputargument(self, obj):
        for key in obj.__dict__.keys():
            if key != "strategy":
                obj.__dict__[key] = input(key)