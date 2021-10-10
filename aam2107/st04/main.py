from .kartoteka import MenuKartoteka


archive = MenuKartoteka()

container = {
    1: ("Добавить элемент", archive.add),
    2: ("Редактировать", archive.change),
    3: ("Вывести элемент на экран", archive.print),
    4: ("Выгрузить в файл", archive.file_write),
    5: ("Загрузить из файла", archive.file_read),
    6: ("Очистить", archive.clear),
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
