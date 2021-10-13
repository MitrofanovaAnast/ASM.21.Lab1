if __name__ == '__main__':
    from group import group
    from objects.rgu import rgu
else:
    from .group import group
    from .objects.rgu import rgu
    from .objects.worker import worker
    from .objects.student import student
    from .objects.starosta import starosta
    from .objects.zavkaf import zavkaf

    from .strategies.storage import PickleStorage
    from .strategies.strategy import Strategy

def show_menu():
    print('Выберите действие:\n'
          '1. Вывести список\n'
          '2. Добавить запись\n'
          '3. Очистить список\n'
          '4. Поиск\n'
          '5. Выход\n')

def main():
    while True:
        RGU=rgu(PickleStorage)
        show_menu()
        choice=int(input())
        if choice==1:
            choice2=int(input('1. Всех записей\n'
                              '2. Записей студентов\n'
                              '3. Записей сотрудников\n'))
            if choice2==1:
                # print('asdsa')
                for member in RGU.members.values():
                    # pass
                    member.get()
            else:
                for member in RGU.members.values():
                    if choice2==2 and isinstance(member, student):
                        member.get()
                    elif choice2==3 and isinstance(member, worker):
                        member.get()
        elif choice==2:
            choice2=int(input('1. Студента\n'
                              '2. Старосту\n'
                              '3. Служащего\n'
                              '4. Заведующего кафедрой\n'))
            if choice2==1:
                member=student(Strategy)
            elif choice2==2:
                member=starosta(Strategy)
            elif choice2==3:
                member=worker(Strategy)
            elif choice2==4:
                member=zavkaf(Strategy)
            else:
                continue

            member.set()
            RGU.append(member)
        elif choice==3:
            RGU.clear()
        elif choice==4:
            choice2=int(input('1. По имени\n'
                              '2. По номеру\n'))
            if choice2==1:
                name=input('Введите имя\n')
                find=RGU.search_by_name(name)
            elif choice2==2:
                id=int(input('Введите номер\n'))
                find=RGU.search_by_id(id)
            else:
                continue

            if find is not None:
                print(str(find))
            else:
                print('Не найдено\n')
        elif choice==5:
            break
        else:
            continue
        RGU.save()




if __name__ == '__main__':
    main()


