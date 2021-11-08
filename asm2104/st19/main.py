if __name__ == '__main__':
    from group import group
else:
    from .group import group
    #Models
    from .student import student
    from .worker import worker
    from .starosta import starosta
    from .chef import chef
    #Strategys
    from .storage import storagePickle
    from .interactive import interactiveConsole

    #container
    from .kartoteka import kartoteka


def choice():
    text=f'Choice action:\n' \
         f'1. Add user\n' \
         f'2. Show users\n' \
         f'3. Clear users\n' \
         f'4. Search user\n' \
         f'5. Exit\n'
    return int(input(text))


cont=kartoteka()


def add():
    try:
        cont.load(storagePickle)
    except:
        pass

    ch2 = int(input('1. Student\n'
                    '2. Starosta\n'
                    '3. Worker\n'
                    '4. Chef\n'))
    if ch2 == 1:
        buff = student()
    elif ch2 == 2:
        buff = starosta()
    elif ch2 == 3:
        buff = worker()
    elif ch2 == 4:
        buff = chef()
    else:
        return

    buff.input(interactiveConsole)
    # member.output(Console)
    index = cont.add_member(buff)
    print(f'User number: {index}\n')

    cont.store(storagePickle)

def show():
    try:
        cont.load(storagePickle)
    except:
        pass

    ch2 = int(input('1. Students\n'
                    '2. Workers\n'
                    '3. All users\n'))
    if ch2 == 1:
        for user in cont.container.values():
            if user.type=='student':
                user.output(interactiveConsole)
            # if isinstance(user, student):
            #     user.output(interactiveConsole)
    elif ch2 == 2:
        for user in cont.container.values():
            if user.type=='worker':
                user.output(interactiveConsole)
            # if isinstance(user, worker):
            #     user.output(interactiveConsole)
    elif ch2 == 3:
        for user in cont.container.values():
            user.output(interactiveConsole)

def clear():
    cont.clr()
    cont.store(storagePickle)

def search():
    try:
        cont.load(storagePickle)
    except: pass

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


menu={
    1:['Add user', add],
    2:['Show users', show],
    3:['Clear', clear],
    4:['Search', search],
    5:['Exit']
}






def main():
    while True:
        try:
            for key, value in menu.items():
                print(f'{key}. {value[0]}')

            choice=int(input())
            if choice==5:
                break
            elif choice<1 or choice>5:
                continue
            else:
                menu[choice][1]()

        except: continue
        # cont = kartoteka()
        # # try
        # # cont.load(PickleStorage)
        # try:
        #     cont.load(storagePickle)
        # except:
        #     pass
        #
        #
        #
        # try:
        #     p=choice()
        #     if p==1:
        #         ch2 = int(input('1. Student\n'
        #                         '2. Starosta\n'
        #                         '3. Worker\n'
        #                         '4. Chef\n'))
        #         if ch2 == 1:
        #             buff = student()
        #         elif ch2 == 2:
        #             buff = starosta()
        #         elif ch2 == 3:
        #             buff = worker()
        #         elif ch2 == 4:
        #             buff = chef()
        #         else:
        #             continue
        #
        #         buff.input(interactiveConsole)
        #         # member.output(Console)
        #         index = cont.add_member(buff)
        #         print(f'User number: {index}\n')
        #     elif p==2:
        #         ch2 = int(input('1. Students\n'
        #                         '2. Workers\n'
        #                         '3. All users\n'))
        #         if ch2 == 1:
        #             for user in cont.container.values():
        #                 if isinstance(user, student):
        #                     user.output(interactiveConsole)
        #         elif ch2 == 2:
        #             for user in cont.container.values():
        #                 if isinstance(user, worker):
        #                     user.output(interactiveConsole)
        #         elif ch2 == 3:
        #             for user in cont.container.values():
        #                 user.output(interactiveConsole)
        #     elif p==3:
        #         cont.clr()
        #     elif p==4:
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
        #     elif p==5:
        #         break
        #     else:
        #         continue
        #
        #     cont.store(storagePickle)
        # except: continue


if __name__ == '__main__':
    main()


