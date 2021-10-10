from asm2104.st06.ConsoleIO import ConsoleIO
from asm2104.st06.Manager import Manager
from asm2104.st06.Player import Player
from asm2104.st06.Staff import Staff
from asm2104.st06.StorageIO import Pickle, Shelve

member_type = {
    1: ('Add player', Player),
    2: ('Add staff', Staff),
    3: ('Add Manager', Manager)
}

strategy_dict = {
    1: ('Console', ConsoleIO),
    2: ('Pickle', Pickle),
    3: ('Shelve', Shelve),
}


class Team:

    def __init__(self, strategy, members=[]):
        self.members = members
        self.strategy = strategy

    def add_member(self):
        for i, item in member_type.items():
            print(i, ": ", item[0])
        print("------------------------------")
        sel = int(input())
        self.members.append(member_type[sel][1]())

    def display_members(self):
        ConsoleIO.dump(self.members)

    def __set_strategy(self):
        print('Choose strategy:')
        for i, item in strategy_dict.items():
            print(i, ": ", item[0])
        print("------------------------------")
        inp = int(input())
        self.strategy = strategy_dict[inp][1]()

    def dump(self):
        self.__set_strategy()
        self.strategy.dump(self.members)

    def load(self):
        self.__set_strategy()
        self.members = self.strategy.load(self.members)

    def delete_members(self):
        self.members.clear()

    def edit_member(self):
        print('Choose member to edit:')
        edit_num = int(input())
        for i, item in member_type.items():
            print(i, ": ", item[0])
        print("------------------------------")
        sel = int(input())
        self.members.pop(edit_num)
        self.members.insert(edit_num, member_type[sel][1]())
