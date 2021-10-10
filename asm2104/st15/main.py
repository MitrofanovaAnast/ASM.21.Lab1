from .shop import Shop

shop = Shop()
menu = [
    {'label': 'Добавить сотрудников', 'method': shop.addEmployee},
    {'label': 'Очистить сотрудников', 'method': shop.clearEmployees},
    {'label': 'Записать/вывести', 'method': shop.showEmployees},
    {'label': 'Считать', 'method': shop.getEmployees},
    {'label': 'Изменить стратегию', 'method': shop.changeStrategy},
    {'label': 'Выйти'},
]


def main():
    while True:
        for i in range(len(menu)):
            print('{0}. {1}'.format(i, menu[i]['label']))
        try:
            selected = int(input())
            if selected == 5:
                return
            menu[selected]['method']()
        except:
            print('Введите число от 0 до {}'.format(len(menu) - 1))


if __name__ == '__main__':
    main()
