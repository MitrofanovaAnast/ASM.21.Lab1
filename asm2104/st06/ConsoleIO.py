from asm2104.st06.Manager import Manager
from asm2104.st06.Player import Player
from asm2104.st06.Staff import Staff

member_type = {
    1: ('Add player', Player),
    2: ('Add staff', Staff),
    3: ('Add Manager', Manager)
}


class ConsoleIO:

    @staticmethod
    def dump(list):
        for member in list:
            print(member)
            print('________________\n')

    @staticmethod
    def load(list):
        print('Choose member you want to add:')
        for i, item in member_type.items():
            print(i, ": ", item[0])
        print("------------------------------")
        s = int(input())
        list.append(member_type[s][1]())
        return list