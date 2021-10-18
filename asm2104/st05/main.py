"""
Работа: Ерыгина Светлана АСМ 21-04
Запуск осуществляется из данного модуля.
CMD: python main.py

person.py - Описание сущностей
pickleStrategy.py - Описание стратегий хранения
inp_out.py - Описание стратегий ввода вывода
group.py - контекст

"""

if __name__ == '__main__':
    from group import Group
    from inp_out import InputOutPutConsole
    from storage import InputOutPutFile
else:
    from .group import Group
    from .inp_out import InputOutPutConsole
    from .storage import InputOutPutFile


def create_actions_group() -> dict:
    group = Group(strategy_io=InputOutPutConsole(),
                  strategy_storage=InputOutPutFile())
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
          '2.  Редактировать участника\n'
          '3.  Удалить всех участников\n'
          '4.  Вывести на экран весь список\n'
          '5.  Сохранить в файл\n'
          '6.  Загрузить из файла\n'
          'Нажмите q для входа')
    print("--------------------------------------------------\n")


def main():
    menu()
    action = create_actions_group()

    try:
        while True:
            print('Введите действие:')
            act = input()
            if act == 'q':
                print(f"Программа завершена.")
                break
            action[int(act)]()
    except KeyError as key:
        print(f"Было введено неверное действие: {key}")
    except Exception as e:
        print(f"Программа завершена с ошибкой: {e}")


if __name__ == '__main__':
    main()


