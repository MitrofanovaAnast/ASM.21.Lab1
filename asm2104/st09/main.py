from .company import Company


company = Company([])
menuList = [
    {'label': 'Добавить элементы вручную', 'handler': company.addElements},
    {'label': 'Вывести список элементов в консоль', 'handler': company.printElements},
    {'label': 'Загрудить из файла', 'handler': company.loadElements},
    {'label': 'Сохранить в файл', 'handler': company.saveElements},
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
