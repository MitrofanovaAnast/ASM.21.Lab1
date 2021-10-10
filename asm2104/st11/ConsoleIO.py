from asm2104.st11.Developer import Developer
from asm2104.st11.Lead import Lead

employee_type = [
    {'title': 'Add lead', 'class': Lead},
    {'title': 'Add developer', 'class': Developer}
]


class ConsoleIO:

    @staticmethod
    def output(e_list):
        for i in e_list:
            print(i)

    @staticmethod
    def input(lenght, e_list):
        print('Choose who to add:')
        for i in range(len(employee_type)):
            print('{0}. {1}'.format(i + 1, employee_type[i]['title']))
        select = int(input()) - 1
        if 0 <= select < len(employee_type):
            e_list.append(employee_type[select]['class'](lenght))
        else:
            print('This menu item does not exist')
        return e_list
