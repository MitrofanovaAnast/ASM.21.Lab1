from kartoteka import MenuCartoteka

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
    print("------------------------------")
    for i, item in container.items():
        print(i, ": ", item[0])
    print("------------------------------")
    return int(input())


if __name__ == '__main__':
    try:
        while True:
            container[main()][1]()
    except Exception as ex:
        print(ex, "\nbye")