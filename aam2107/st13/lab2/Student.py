from .Strategy import Strategy


class Student:

    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.name = "name"
        self.group = "group"

    def outputinfo(self):
        return self.strategy.outputinfo(self.name, self.group)

    def inputargument(self, name_argument, argument):
        self.strategy.inputargument(self, name_argument, argument)

    def __str__(self):
        return "Имя: {} \t Группа: {}".format(self.name, self.group)
