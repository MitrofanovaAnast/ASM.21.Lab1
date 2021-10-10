
class listEntry:

    def __init__(self, strategy):
        self.id = -1
        self.name = ''
        self.age = ''
        self.strategy=strategy(self)

    def __str__(self):
        text=f'Номер: {self.id}\n' \
             f'Имя: {self.name}\n' \
             f'Возраст: {self.age}\n'
        return text

    def Out(self):
        self.strategy.Out()

    def In(self):
        self.strategy.In()

