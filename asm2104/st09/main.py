from .company import Company


company = Company([])
menuList = [
    {'label': 'Добавить элементы', 'handler': company.setElements},
    {'label': 'Вывести список элементов', 'handler': company.getElements},
    {'label': 'Выбрать стратегию', 'handler': company.chooseStrategy},
    {'label': 'Очистить список элементов', 'handler': company.clearAllElements},
]


def main():
    while True:
        print()
        for i in range(len(menuList)):
            print('{0} - {1}'.format(i, menuList[i]['label']))
        menuList[int(input())]['handler']()


if __name__ == '__main__':
    main()
