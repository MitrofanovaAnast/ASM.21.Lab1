if __name__ == '__main__':
    from group import group
else:
    from .group import group

from .app.Objects.RGU import RGU
from .app.Objects.Student import Student
from .app.Objects.Starosta import Starosta
from .app.Objects.Staff import Staff
from .app.Objects.Decan import Decan
from .app.Strategies.GetSet import ConsoleGetSet
from .app.Strategies.Storage import PickleStorage

def show_menu():
    print('Что Вы хотите сделать?:\n'
          '1. Посмотреть\n'
          '2. Добавить\n'
          '3. Поиск по номеру\n'
          '4. Удалить все\n')


def main():
    while True:
        try:
            rgu=RGU(PickleStorage)

            show_menu()
            choice=int(input())
            if choice==1:
                text='Какой список вы хотите увидеть?\n' \
                     '1. Все\n' \
                     '2. Студенты\n' \
                     '3. Только старосты\n' \
                     '4. Сотрудники\n' \
                     '5. Деканы\n'
                inp=int(input(text))
                if inp==1:
                    for member in rgu.members.values():
                        member.print()
                        print('---\n')
                elif inp==2:
                    for member in rgu.members.values():
                        if isinstance(member, Student):
                            member.print()
                            print('---\n')
                elif inp==3:
                    for member in rgu.members.values():
                        if isinstance(member, Starosta):
                            member.print()
                            print('---\n')
                elif inp==4:
                    for member in rgu.members.values():
                        if isinstance(member, Staff):
                            member.print()
                            print('---\n')
                elif inp==5:
                    for member in rgu.members.values():
                        if isinstance(member, Decan):
                            member.print()
                            print('---\n')

            elif choice==2:
                text = 'Кого Вы хотите добавить?\n' \
                       '1. Студент\n' \
                       '2. Староста\n' \
                       '3. Сотрудник\n' \
                       '4. Декан\n'

                inp=int(input(text))
                if inp==1:
                    obj=Student(ConsoleGetSet)
                elif inp==2:
                    obj=Starosta(ConsoleGetSet)
                elif inp==3:
                    obj=Staff(ConsoleGetSet)
                elif inp==4:
                    obj=Decan(ConsoleGetSet)
                else:
                    continue

                obj.set()
                rgu.add_member(obj)
            elif choice==3:
                number=input('Введите номер\n')
                member=rgu.get_by_num(number)
                if member is not None:
                    print(str(member))
                else:
                    print('Человек не найден')

            elif choice==4:
                rgu.clear()

            else:
                continue

            rgu.save()
        except:
            pass





if __name__ == '__main__':
    main()


