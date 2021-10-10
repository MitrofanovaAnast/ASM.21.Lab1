from asm2104.st11.ConsoleIO import ConsoleIO
from asm2104.st11.Developer import Developer
from asm2104.st11.FileIO import FileIO
from asm2104.st11.Lead import Lead

employee_type = [
    {'title': 'Add lead', 'class': Lead},
    {'title': 'Add developer', 'class': Developer}
]

io_type = [
    {'title': 'File', 'class': FileIO},
    {'title': 'Console', 'class': ConsoleIO}
]


class Company:
    strategy = ConsoleIO

    def __init__(self):
        self.employee_list = list()

    def add_employee(self):
        self.lenght = len(self.employee_list)
        print('Choose who to add:')
        for i in range(len(employee_type)):
            print('{0}. {1}'.format(i + 1, employee_type[i]['title']))
        select = int(input()) - 1
        if 0 <= select < len(employee_type):
            self.employee_list.append(employee_type[select]['class'](self.lenght))
        else:
            print('This menu item does not exist')

    def show_employee_list(self):
        ConsoleIO.output(self.employee_list)

    def change_strategy(self):
        print('Select output')
        for i in range(len(io_type)):
            print('{0}. {1}'.format(i + 1, io_type[i]['title']))
        select = int(input()) - 1
        if 0 <= select < len(io_type):
            self.strategy = io_type[select]['class']
        else:
            print('This menu item does not exist')

    def clear_employee_list(self):
        print('Do you really want to clear the data?\nPress 9 to confirm or any button to cancel')
        select = int(input())
        if select == 9:
            self.employee_list.clear()
        else:
            pass

    def output(self):
        self.change_strategy()
        self.strategy.output(self.employee_list)

    def input(self):
        self.lenght = len(self.employee_list)
        self.change_strategy()
        self.employee_list = self.strategy.input(self.lenght, self.employee_list)

    def edit_employee(self):
        print('Choose employee ID to edit:')
        e_select = int(input()) - 1
        for i in range(len(employee_type)):
            print('{0}. {1}'.format(i + 1, employee_type[i]['title']))
        select = int(input()) - 1
        if 0 <= select < len(employee_type):
            self.employee_list[e_select] = employee_type[select]['class'](e_select)
        else:
            print('This menu item does not exist')
