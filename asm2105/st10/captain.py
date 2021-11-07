from asm2105.st10.player import Player


class Captain(Player):
    def __init__(self):
        super(Captain, self).__init__()
        self.age = input('Введите возраст\n')

    def __str__(self):
        return super(Captain, self).__str__() + f'Возраст: {self.age}'
