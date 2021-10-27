import sys
from strategy_storage import Storage
from strategy_io import IO
from student import Student
from headmen import Headmen


class Group:
    members = []

    def __init__(self, strategy_io: IO, strategy_storage: Storage):
        self._strategy_io = strategy_io
        self._strategy_storage = strategy_storage

    def add_member(self):
        """
        Добавить пользователя в базу
        :return:
        """
        case = int(input("0 - Студент, 1  - Староста: \n"))
        person = Headmen() if case else Student()
        self.member_from_console(person)
        self.members.append(person)

    def member_from_console(self, person):
        """
        Записать пользователя из консоли
        :param person:
        :return:
        """
        self._strategy_io.enter(person)

    def members_in_console(self):
        """
        Вывести в консоль всех пользователей
        :return:
        """
        self._strategy_io.output(self.members)

    def members_from_file(self):
        """
        Записать пользователя из файла
        :return:
        """
        self.members = self._strategy_storage.input()

    def members_in_file(self):
        """
        Записать пользователя
        :return:
        """
        self._strategy_storage.output(self.members)

    def delete_members(self):
        """
        Удалить всех пользователей
        :return:
        """
        del self.members[:]

    def edit_members(self):
        """
        Изменение пользователя
        :return:
        """
        print('Пожалуйста, укажите id пользователя')
        try:
            case = int(input("Введите натуральное число"))
        except ValueError:
            print("Вы не ввели натуральное число")
            sys.exit()
        try:
            person = self.members[case]
        except IndexError:
            print(f"Не удалось найти такое id :{case}")
            sys.exit()
        self.member_from_console(person)
