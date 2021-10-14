if __name__ == '__main__':
    from group import group
else:
    from .group import group
    from .file import file
    from .student import student
    from .leader import leader
    from .employe import employe
    from .teacher import teacher
    from .director import director
    from .storage import PickleStorage
    from .console import Console


def main():
    while True:
        fl=file()
        fl.load(PickleStorage)
        # try:
            # fl.load(PickleStorage)
        # except:pass
        ch=int(input('1. Добавить\n'
                     '2. Поиск\n'
                     '3. Просмотр\n'
                     '4. Очистка\n'
                     '5. Выйход\n'))
        if ch==1:
            ch2=int(input('1. Студент\n'
                    '2. Староста\n'
                    '3. Преподаватель\n'
                    '4. Директор\n'))
            if ch2==1:
                member=student()
            elif ch2==2:
                member=leader()
            elif ch2==3:
                member=teacher()
            elif ch2==4:
                member=director()
            else:
                continue

            member.input(Console)
            # member.output(Console)
            fl.add_member(member)
        elif ch==2:
            param=input('Введите ID или Name\n')
            obj=fl.get_member(param)
            if obj is not None:
                if isinstance(obj, list):
                    for o in obj:
                        print(str(o))
                else:
                    print(str(obj))
            else:
                continue
        elif ch==3:
            ch2 = int(input('1. Студентов\n'
                            '2. Работников\n'
                            '3. Всех\n'))
            if ch2==1:
                for member in fl.members:
                    if isinstance(member, student):
                        member.output(Console)
            elif ch2==2:
                for member in fl.members:
                    if isinstance(member, employe):
                        member.output(Console)
            elif ch2==3:
                for member in fl.members:
                    member.output(Console)
        elif ch==4:
            fl.clr()
        elif ch==5:
            break
        else: continue

        fl.store(PickleStorage)




if __name__ == '__main__':
    main()


