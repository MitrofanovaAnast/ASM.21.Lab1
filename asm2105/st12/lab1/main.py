if __name__ == '__main__':
    from kartoteka import MenuCartoteka
else:
    from .kartoteka import MenuCartoteka

cart = MenuCartoteka()
container = {
    1: ("Добавить элемент", cart.add),
    2: ("Вывести элемент на экран", cart.print),
    3: ("Выгрузить в файл", cart.file_read),
    4: ("Загрузить из файла", cart.file_write),
    5: ("Очистить", cart.clear),
    6: ("Редактировать", cart.change),
}


def main():
    try:
        while True:
            print("------------------------------")
            for i, item in container.items():
                print(i, ": ", item[0])
            print("------------------------------")
            container[int(input())][1]()
    except Exception as ex:
        print(ex, "\nbye")

if __name__ == '__main__':
    main()
