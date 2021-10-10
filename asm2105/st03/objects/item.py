
class item:
    id=-1
    name=''
    age=int()

    def __init__(self, strategy):
        self.strategy=strategy

    def __str__(self):
        text=f'Номер: {self.id}\n' \
             f'Имя: {self.name}\n' \
             f'Возраст: {self.age}\n'
        return text

    def set(self):
        pass

    def get(self):
        pass