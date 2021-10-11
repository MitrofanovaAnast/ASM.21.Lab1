if __name__ == '__main__':
    from group import Group
    from StrategyIO import ConsoleIO
    from StrategyFileIO import FileIO
else:
    from .group import Group
    from .StrategyIO import ConsoleIO
    from .StrategyFileIO import FileIO



def menu():
    print( '1.  Добавить персонажа в картотеку и выбрать доп образование\n'
           '2.  Вывести всех персонажей из картотеки\n'
           '3.  Удалить всех участников\n'
           '4.  Редактировать участника\n'
           '5.  Сохранить в файл\n'
           '6.  Загрузить из файла\n'
           'w - для закрытия программы')


def main():
    menu()
    group = Group(strategyFile = FileIO(), strategyIO = ConsoleIO())
    actions = {
        1: group.addStudent,
        2: group.print_cartoteka,
        3: group.clear_kartoteka,
        4: group.cartoteka_edit_person,
        5: group.cartoteka_in_file,
        6: group.cartoteka_from_file,
    }
    try:
        while True:
            print('Введите действие: ')
            id_action = input()
            if id_action == 'w':
                break
            actions[int(id_action)]()
    except KeyError:
        print('Неверная команда')




if __name__ == '__main__':
	main()


