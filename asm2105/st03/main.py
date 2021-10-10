if __name__ == '__main__':
    from group import group
    from objects.rgu import rgu
else:
    from .group import group
    from .objects.rgu import rgu

def show_menu():
    print('Выберите действие:\n'
          '1. Вывести список\n'
          '2. Добавить\n'
          '3. Очистить\n'
          '4. Поиск\n'
          '5. Выход\n')

def main():
    while True:
        show_menu()
        choice=int(input())

        if choice==5:
            break




if __name__ == '__main__':
    main()


