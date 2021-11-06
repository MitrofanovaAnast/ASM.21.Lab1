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


def show(rgu):
    choice = int(input('1. Всех записей\n'
                        '2. Записей студентов\n'
                        '3. Записей сотрудников\n'))
    if choice == 1:
        for member in rgu.members.values():
            member.get()
    else:
        for member in rgu.members.values():
            if choice == 2 and member.type == 'student':
                member.get()
            elif choice == 3 and member.type == 'worker':
                member.get()


    # if type is None:
    #     for member in rgu.members.values():
    #         member.get()
    # else:
    #     for member in rgu.members.values():
    #         if member.type==type:
    #             member.get()

def add(rgu):
    choice = int(input('1. Студента\n'
                        '2. Старосту\n'
                        '3. Служащего\n'
                        '4. Заведующего кафедрой\n'))
    if choice == 1:
        member = student(Strategy)
    elif choice == 2:
        member = starosta(Strategy)
    elif choice == 3:
        member = worker(Strategy)
    elif choice == 4:
        member = zavkaf(Strategy)
    else:
        return

    member.set()
    rgu.append(member)

def clear(rgu):
    rgu.clear()

def search(rgu):
    choice = int(input('1. По имени\n'
                        '2. По номеру\n'))
    if choice == 1:
        name = input('Введите имя\n')
        find = rgu.search_by_name(name)
    elif choice == 2:
        id = int(input('Введите номер\n'))
        find = rgu.search_by_id(id)
    else:
        return

    if find is not None:
        print(str(find))
    else:
        print('Не найдено\n')


menu={
    1:['Вывести список', show],
    2:['Добавить запись', add],
    3:['Очистить список', clear],
    4:['Поиск', search],
    5:['Выход']
}

def main():
    while True:
        RGU = rgu(PickleStorage)

        for key, value in menu.items():
            print(f'{key}. {value[0]}')

        choice=int(input())
        if choice==5:
            break
        else:
            menu[choice][1](RGU)
            RGU.save()




        # RGU=rgu(PickleStorage)
        # show_menu()
        # choice=int(input())
        # if choice==1:
        #     choice2=int(input('1. Всех записей\n'
        #                       '2. Записей студентов\n'
        #                       '3. Записей сотрудников\n'))
        #     if choice2==1:
        #         # print('asdsa')
        #         for member in RGU.members.values():
        #             # pass
        #             member.get()
        #     else:
        #         for member in RGU.members.values():
        #             if choice2==2 and member.type=='student':
        #                 member.get()
        #             elif choice2==3 and member.type=='worker':
        #                 member.get()
        # elif choice==2:
        #     choice2=int(input('1. Студента\n'
        #                       '2. Старосту\n'
        #                       '3. Служащего\n'
        #                       '4. Заведующего кафедрой\n'))
        #     if choice2==1:
        #         member=student(Strategy)
        #     elif choice2==2:
        #         member=starosta(Strategy)
        #     elif choice2==3:
        #         member=worker(Strategy)
        #     elif choice2==4:
        #         member=zavkaf(Strategy)
        #     else:
        #         continue
        #
        #     member.set()
        #     RGU.append(member)
        # elif choice==3:
        #     RGU.clear()
        # elif choice==4:
        #     choice2=int(input('1. По имени\n'
        #                       '2. По номеру\n'))
        #     if choice2==1:
        #         name=input('Введите имя\n')
        #         find=RGU.search_by_name(name)
        #     elif choice2==2:
        #         id=int(input('Введите номер\n'))
        #         find=RGU.search_by_id(id)
        #     else:
        #         continue
        #
        #     if find is not None:
        #         print(str(find))
        #     else:
        #         print('Не найдено\n')
        # elif choice==5:
        #     break
        # else:
        #     continue
        # RGU.save()




if __name__ == '__main__':
    main()


