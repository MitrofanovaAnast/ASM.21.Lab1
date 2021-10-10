if __name__ == '__main__':
    from group import group
    from model.school import school
    from strategy.Storage import Pickle
else:
    from .group import group
    from .model.school import school
    from .strategy.Storage import Pickle
    from .strategy.Interaction import ConsoleInteraction
    from .model.student import student
    from .model.starosta import starosta
    from .model.worker import worker
    from .model.teacher import teacher
    from .model.director import director


def get_choice():
    print('Выберите действие:\n'
          '1. Посмотреть\n'
          '2. Добавить\n'
          '3. Поиск\n'
          '4. Очистить\n'
          '5. Выход')
    return int(input())


def main():
    while True:
        cont=school(Pickle)
        choice=get_choice()
        if choice==1:
            inp=int(input('1. Ученики\n'
                          '2. Старосты\n'
                          '3. Сотрудники\n'
                          '4. Учителя\n'
                          '5. Директоры\n'
                          '6. Весь список\n'))

            for i in cont.list.values():
                if inp==1 and isinstance(i, student):
                    i.Out()
                elif inp==2 and isinstance(i, starosta):
                    i.Out()
                elif inp==3 and isinstance(i, worker):
                    i.Out()
                elif inp==4 and isinstance(i, teacher):
                    i.Out()
                elif inp==5 and isinstance(i, director):
                    i.Out()
                elif inp==6:
                    i.Out()
        elif choice==2:
            inp = int(input('1. Ученик\n'
                            '2. Староста\n'
                            '3. Сотрудник\n'
                            '4. Учитель\n'
                            '5. Директор\n'))
            if inp==1:
                obj=student(ConsoleInteraction)
            elif inp==2:
                obj=starosta(ConsoleInteraction)
            elif inp==3:
                obj=worker(ConsoleInteraction)
            elif inp==4:
                obj=teacher(ConsoleInteraction)
            elif inp==5:
                obj=director(ConsoleInteraction)
            else: continue

            obj.In()
            cont.add(obj)
        elif choice==3:
            param=input('Введите имя или номер')
            print(str(cont.search(param)))
        elif choice==4:
            cont.clear()
        elif choice==5:
            break
        else:
            continue

        cont.save()



if __name__ == '__main__':
    main()


