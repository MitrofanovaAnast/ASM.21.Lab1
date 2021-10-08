from abc import ABC, abstractmethod
import pickle, shelve


class Strategy(ABC):

    @abstractmethod
    def outputinfo(self, name, group):
        pass

    @abstractmethod
    def inputargument(self, obj, name_argument, argument) -> None:
        setattr(obj, name_argument, argument)


class ConcreteStrategyStudent(Strategy):
    def outputinfo(self, name, group) -> str:
        return "Имя: {} \t Группа: {}".format(name, group)

    def inputargument(self, obj, name_argument: str, argument):
        super().inputargument(obj, name_argument, argument)


class ConcreateStrategyStarosta(Strategy):
    def outputinfo(self, name, group, doppole) -> str:
        return "Имя: {} \t Группа: {} \t Допполе: {}".format(name, group, doppole)

    def inputargument(self, obj, name_argument: str, argument):
        super().inputargument(obj, name_argument, argument)


class FileStrategy(ABC):
    @abstractmethod
    def fileoutput(self, obj) -> None:
        pass

    @abstractmethod
    def fileinput(self, obj) -> None:
        pass


class PickleStategy(FileStrategy):
    def fileoutput(self, obj):
        pickle.dump(obj, open("data.dat", "wb"))

    def fileinput(self):
        obj = pickle.load(open("data.dat", "rb"))
        return obj


class ShelveStrategy(FileStrategy):
    def fileoutput(self, obj: list):
        d = shelve.open("shdata.dat")
        for id, v in enumerate(obj):
            d[str(id)] = v
        d.close()

    def fileinput(self):
        pass