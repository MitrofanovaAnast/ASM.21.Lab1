# if __name__ == '__main__':
#     from group import group
# else:
#     from .group import group
#
import sys

from asm2104.st06 import ConsoleIO
from asm2104.st06.Team import Team

Team = Team()

act_menu = {
    1: ('Add member', Team.add_member),
    2: ('Load', Team.load),
    3: ('Dump', Team.dump),
    4: ('Show all members', Team.display_members),
    5: ('Delete members', Team.delete_members),
    6: ('Edit member', Team.edit_member),
    7: ('Exit', sys.exit)
    }


def main():
    while True:
        for i, item in act_menu.items():
            print(i, ": ", item[0])
        print("------------------------------")
        selected = int(input())
        act_menu[selected][1]()




if __name__ == '__main__':
    main()
