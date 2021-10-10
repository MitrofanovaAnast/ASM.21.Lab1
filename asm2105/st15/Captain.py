if __name__ == '__main__':
    from Player import Player
else:
    from .Player import Player


class Captain(Player):
    def __init__(self, name=' ', surname=' ', age=' ', experience=' '):
        super().__init__(name, surname, age)
        self.experience = experience;

    def write_data(self):
        Player.write_data(self)
        self.experience = input("Опыт: ", )

    def __str__(self):
        return super().__str__()+ f'\nОпыт: {self.experience}'


