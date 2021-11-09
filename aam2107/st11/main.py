from .pharmacy import Pharmacy

pharmacy = Pharmacy()
menu = [
    {'label': 'Добавить фармацевтов', 'method': pharmacy.addEmployee},
    {'label': 'Очистить фармацевтов', 'method': pharmacy.clearEmployees},
    {'label': 'Записать/вывести', 'method': pharmacy.showEmployees},
    {'label': 'Считать', 'method': pharmacy.getEmployees},
    {'label': 'Изменить метод', 'method': pharmacy.changeStrategy},
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
