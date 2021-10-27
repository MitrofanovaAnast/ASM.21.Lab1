if __name__ == '__main__':
    from group import Group
    from strategy_io import ConsoleInputOutPut
    from strategy_storage import FileInputOutPut
else:
    from .group import Group
    from .strategy_io import ConsoleInputOutPut
    from .strategy_storage import FileInputOutPut


def create_group() -> dict:
    group = Group(strategy_io=ConsoleInputOutPut(),
                  strategy_storage=FileInputOutPut())
    actions = {
        1: group.add_member,
        2: group.edit_members,
        3: group.delete_members,
        4: group.members_in_console,
        5: group.members_in_file,
        6: group.members_from_file,
    }
    return actions


def menu():
    print('Menu', end="--------------------------------------------------\n")
    print('1.  Добавить объект выбранного типа\n'
          '2.  Редактировать пользователя\n'
          '3.  Удалить из базы всех пользователей\n'
          '4.  Показать весь список\n'
          '5.  Сохранить в файл\n'
          '6.  Загрузить из файла\n'
          'Нажмите q чтобы выйти')
    print("--------------------------------------------------\n")


def main():
    menu()
    action = create_group()

    try:
        while True:
            print('Необходимо ввести действие:')
            act = input()
            if act == 'q':
                print(f"Завершение программы")
                break
            action[int(act)]()
    except Exception as e:
        print(f"Ошибка! Завершение программы {e}")


if __name__ == '__main__':
    main()


