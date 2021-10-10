if __name__ == '__main__':
    from group import group
else:
    from .group import group

from .app.models.university import university
from .app.strategys.storageStrategy import PickleStorageStrategy
from .app.models.workers.worker import worker
from .app.models.students.student import student
from .app.models.students.headman import headman
from .app.models.workers.teacher import teacher


def get_menu():
    text='Выберите действие:\n' \
         '1. Посмотреть всех\n' \
         '2. Посмотреть служащих\n' \
         '3. Посмотреть стуентов\n' \
         '4. Поиск по имени\n' \
         '5. Поиск по номеру\n' \
         '6. Добавить cardItem\n' \
         '7. Удалить все\n' \
         '8. Выход\n'
    return text


def main():
    while True:
        univer = university(PickleStorageStrategy())
        try:
            choice = int(input(get_menu()))
            if choice == 1:
                if len(univer.get_users()) == 0:
                    print('Никого нет')
                else:
                    for user in univer.get_users().values():
                        user.print()
                        print('=======\n')

                    print(f'Колическтво пользователей: {len(univer.get_users())}\n')
            elif choice == 2:
                count = 0
                for user in univer.get_users().values():
                    if isinstance(user, worker):
                        user.print()
                        count += 1

                print(f'Количество сотрудников: {count}\n')

            elif choice == 3:
                count = 0
                for user in univer.get_users().values():
                    if isinstance(user, student):
                        user.print()
                        count += 1

                print(f'Колическтво студентов: {count}\n')

            elif choice == 4:
                name = input('Введите имя')
                find = univer.get_user_or_none_by_name(name)
                if find is not None:
                    for item in find:
                        item.print()
                else:
                    print('Не удалось найти')


            elif choice == 5:
                id = int(input('Введите номер'))
                find = univer.get_user_or_none_by_id(id)
                if find is not None:
                    find.print()
                    choice = int(input('1. Изменить\n'))
                    if choice == 1:
                        find.set_data(find.get_attribs())
                else:
                    print('Не удалось найти')
            elif choice == 6:
                type = int(input('Кого вы хотите добавить?\n'
                                 '1. Студент\n'
                                 '2. Староста\n'
                                 '3. Сотрудник\n'
                                 '4. Преподаватель\n'))
                if type == 1:
                    obj = student()
                elif type == 2:
                    obj = headman()
                elif type == 3:
                    obj = worker()
                elif type == 4:
                    obj = teacher()
                else:
                    continue

                obj.set_data(obj.get_attribs())
                # obj.print()
                univer.append_user(obj)


            elif choice == 7:
                univer.clear()
            elif choice==8:
                break

            else:
                continue

            univer.save()
        except Exception as err:
            print(f'Произошла ошибка: {err}\n'
                  f'Попрбуйте еще раз\n')


if __name__ == '__main__':
    main()


