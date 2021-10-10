from asm2104.st11.Company import Company

comapny = Company()

menu = [
    {'title': 'Add employee', 'method': comapny.add_employee},
    {'title': 'Edit', 'method': comapny.edit_employee},
    {'title': 'Clear', 'method': comapny.clear_employee_list},
    {'title': 'Show all employees', 'method': comapny.show_employee_list},
    {'title': 'Save', 'method': comapny.output},
    {'title': 'Load', 'method': comapny.input},
]


def main():
    while True:
        for i in range(len(menu)):
            print('{0}. {1}'.format(i+1, menu[i]['title']))
        select = int(input())-1
        if 0 <= select < int(len(menu)):
            menu[select]['method']()
        else:
            print('This menu item does not exist')


if __name__ == '__main__':
    main()
