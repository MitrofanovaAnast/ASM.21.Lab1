
class item:
    def __init__(self, strategy):
        self.id = -1
        self.name = ''
        self.age = int()
        self.strategy=strategy()

    def __str__(self):
        text=f'Номер: {self.id}\n' \
             f'Имя: {self.name}\n' \
             f'Возраст: {self.age}\n'
        return text

    def set(self):
        self.strategy.set(self)

    def get(self):
        self.strategy.get(self)

