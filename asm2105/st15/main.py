if __name__ == '__main__':
    from Team import Team
else:
    from .Team import Team

cart = Team()
container = {
    1: ("Добавить элемент", cart.add),
    2: ("Вывести элемент на экран", cart.showTeam),
    3: ("Сохранить в файл", cart.write_file),
    4: ("Загрузить из файла", cart.read_file),
    5: ("Очистить", cart.clear),
    6: ("Редактировать", cart.edit),
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
        print(ex, "\nзавершение")


if __name__ == '__main__':
    main()
