from asm2105.st10.fileIO import FileIO
from asm2105.st10.consoleIO import ConsoleIO


class FC:
    footballers = []

    def __init__(self):
        pass

    def clearAll(self):
        self.footballers.clear()

    def write(self, strategy):
        self.footballers.extend(strategy.load())

    def read(self, strategy):
        strategy.dump(self.footballers)
