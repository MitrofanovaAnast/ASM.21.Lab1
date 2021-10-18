if __name__ == '__main__':
    from group import group
else:
    from .group import group
    from .container import container
    from .student import student
    from .starosta import starosta
    from .sluzh import sluzh
    from .teacher import teacher
    from .director import director
    from .pickleStrategy import PickleStorage
    from .consoleStrategy import Console


def main():
    while True:
        cont=container()
        # try
        # cont.load(PickleStorage)
        try:
            cont.load(PickleStorage)
        except:pass
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
                buff=student()
            elif ch2==2:
                buff=starosta()
            elif ch2==3:
                buff=teacher()
            elif ch2==4:
                buff=director()
            else:
                continue

            buff.input(Console)
            # member.output(Console)
            index=cont.add_member(buff)
            print(f'Номер записи: {index}\n')
        elif ch==2:
            param=input('Введите ID или Name\n')
            obj=cont.get_member(param)
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
                for member in cont.elements:
                    if isinstance(member, student):
                        member.output(Console)
            elif ch2==2:
                for member in cont.elements:
                    if isinstance(member, sluzh):
                        member.output(Console)
            elif ch2==3:
                for member in cont.elements:
                    member.output(Console)
        elif ch==4:
            cont.clr()
        elif ch==5:
            break
        else: continue

        cont.store(PickleStorage)




if __name__ == '__main__':
    main()


