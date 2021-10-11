if __name__ == '__main__':
    from group import group
else:
    from .group import group
    from .models.university import university
    from .strategys.storage import PickleStorage
    from .strategys.interactive import ConsoleInteractive

    from .models.student import student
    from .models.employe import employe
    from .models.decan import decan
    from .models.proforg import proforg


def main():
    while True:
        main_container=university(PickleStorage)
        choice=int(input('1. Посмотреть всех\n'
                         '2. Посмотреть студентов\n'
                         '3. Посмотреть служащих\n'
                         '4. Добавить\n'
                         '5. Поиск по имени\n'
                         '6. Поиск по номеру\n'
                         '7. Очистка\n'
                         '8. Выход\n'))
        if choice==1:
            for item in main_container.items.values():
                item.Print()
        elif choice==2:
            for item in main_container.items.values():
                if isinstance(item, student):
                    item.Print()
        elif choice==3:
            for item in main_container.items.values():
                if isinstance(item, employe):
                    item.Print()
        elif choice==4:
            choice2=int(input('1. Студент\n'
                              '2. Служащий\n'
                              '3. Профорг\n'
                              '4. Декан\n'))
            if choice2==1:
                item=student(ConsoleInteractive)
            elif choice2==2:
                item=employe(ConsoleInteractive)
            elif choice2==3:
                item=proforg(ConsoleInteractive)
            elif choice2==4:
                item=decan(ConsoleInteractive)
            else:
                continue

            item.Enter()
            main_container.addItem(item)
        elif choice==5:
            name=input('Введите имя\n')
            item=main_container.get_by_name(name)
            if item is not None:
                print(item)
        elif choice==6:
            number=int(input('Введите номер\n'))
            item=main_container.get_by_number(number)
            if item is not None:
                print(item)
        elif choice==7:
            main_container.clear()
        elif choice==8:
            break
        else:
            continue

        main_container.dump()



if __name__ == '__main__':
    main()


