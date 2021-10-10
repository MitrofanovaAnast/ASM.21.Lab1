if __name__ == '__main__':
    from Captain import Captain as cap
    from Player import Player as play
else:
    from .Captain import Captain as cap
    from .Player import Player as play

import pickle

class Team:
    def __init__(self):
        self.team = []

    def add(self):
        case = int(input("0 - Игрок, 1  - Капитан: \n"))
        player = cap() if case else play()
        player.write_data()
        self.team.append(player)

    def showTeam(self):
        for (i, player) in enumerate(self.team):
            print('Игрок номер', i + 1)
            player.read_data()

    def edit(self):
        self.showTeam()
        print('Введите номер игрока для редактирования')
        i = int(input())
        self.team[i - 1].write_data()
        print('Игрок номер', i, 'был изменен')

    def delete(self):
        self.showTeam()
        print('Введите номер игрока для удаления')
        i = int(input())
        self.team.pop(i - 1)
        print('Игрок номер', i, 'был удален')

    def write_file(self):
        f = open('team.dat', 'wb')
        pickle.dump(self.team, f)

    def read_file(self):
        f = open('team.dat', 'rb')
        self.team = pickle.load(f)

    def clear(self):
        self.team.clear()
