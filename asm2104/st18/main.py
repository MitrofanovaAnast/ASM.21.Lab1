if __name__ == '__main__':
    from group import group
else:
    from .group import group
    from .allCards import allCards
    from .employe import employe
    from .student import student
    from .teacher import teacher
    from .proforg import proforg
    from .dean import dean
    from .groupLeader import groupLeader
    from .storageStrategy import Pickle
    from .actionStrategy import Console

cont=allCards()

def show():
    try:
        cont.load(Pickle)
    except:pass

    choice = int(input('1. Students\n'
                    '2. Employes\n'
                    '3. All users\n'))
    if choice == 1:
        for user in cont.users:
            if isinstance(user, student):
                user.output(Console)
    elif choice == 2:
        for user in cont.users:
            if isinstance(user, employe):
                user.output(Console)
    elif choice == 3:
        for user in cont.users:
            user.output(Console)

def add():
    try:
        cont.load(Pickle)
    except:pass

    choice = int(input('1. Student\n'
                    '2. Group leader\n'
                    '3. Proforg\n'
                    '4. Teacher\n'
                    '5. Dean\n'))
    if choice == 1:
        buff = student()
    elif choice == 2:
        buff = groupLeader()
    elif choice == 3:
        buff = proforg()
    elif choice == 4:
        buff = teacher()
    elif choice == 5:
        buff = dean()
    else:
        return

    buff.input(Console)
    # member.output(Console)
    index = cont.add_member(buff)
    print(f'User id: {index}\n')

    cont.store(Pickle)

def search():
    try:
        cont.load(Pickle)
    except:pass

    param = input('Input name or id\n')
    obj = cont.get_member(param)
    if obj is not None:
        if isinstance(obj, list):
            for o in obj:
                print(str(o))
        else:
            print(str(obj))
    else:
        return


def clear():
    try:
        cont.load(Pickle)
    except:pass

    cont.clr()
    cont.store(Pickle)


menu={
    1:['Add user', add],
    2:['Search', search],
    3:['Show', show],
    4:['Clear', clear],
    5:['Exit']
}




def main():
    while True:
        try:
            for key, value in menu.items():
                print(key, value[0])

            choice=int(input())
            if choice==5:
                break
            elif choice>5 or choice<1:
                continue
            else:
                menu[choice][1]()
        except:
            continue


        # cont = allCards()
        # # try
        # # cont.load(PickleStorage)
        # try:
        #     cont.load(Pickle)
        # except:
        #     pass
        #
        # try:
        #     choice = int(input('1. Add user\n'
        #                    '2. Search\n'
        #                    '3. Show\n'
        #                    '4. Clear\n'
        #                    '5. Exit\n'))
        #     if choice == 1:
        #         ch2 = int(input('1. Student\n'
        #                         '2. Group leader\n'
        #                         '3. Proforg\n'
        #                         '4. Teacher\n'
        #                         '5. Dean\n'))
        #         if ch2 == 1:
        #             buff = student()
        #         elif ch2 == 2:
        #             buff = groupLeader()
        #         elif ch2 == 3:
        #             buff = proforg()
        #         elif ch2 == 4:
        #             buff = teacher()
        #         elif ch2 == 5:
        #             buff=dean
        #         else:
        #             continue
        #
        #         buff.input(Console)
        #         # member.output(Console)
        #         index = cont.add_member(buff)
        #         print(f'User id: {index}\n')
        #     elif choice == 2:
        #         param = input('Input name or id\n')
        #         obj = cont.get_member(param)
        #         if obj is not None:
        #             if isinstance(obj, list):
        #                 for o in obj:
        #                     print(str(o))
        #             else:
        #                 print(str(obj))
        #         else:
        #             continue
        #     elif choice == 3:
        #         ch2 = int(input('1. Students\n'
        #                         '2. Employes\n'
        #                         '3. All users\n'))
        #         if ch2 == 1:
        #             for user in cont.users:
        #                 if isinstance(user, student):
        #                     user.output(Console)
        #         elif ch2 == 2:
        #             for user in cont.users:
        #                 if isinstance(user, employe):
        #                     user.output(Console)
        #         elif ch2 == 3:
        #             for user in cont.users:
        #                 user.output(Console)
        #     elif choice == 4:
        #         cont.clr()
        #     elif choice == 5:
        #         break
        #     else:
        #         continue
        #
        #     cont.store(Pickle)
        # except: continue


if __name__ == '__main__':
    main()


