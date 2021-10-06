from asm2105.st04.console import MenuInput
from .group import Group

group = Group()

default_menu = [
    {'name': 'Указать название группы', 'func': group.setName},
    {'name': 'Загрузить', 'func': group.loadGroup},
    {'name': 'Завершить работу'}
]

group_menu = [
    {'name': 'Изменить название группы', 'func': group.setName},
    {'name': 'Добавить студента', 'func': group.addStudent},
    {'name': 'Показать всех студентов', 'func': group.showStudents},
    {'name': 'Редактировать студента', 'func': group.editStudent},
    {'name': 'Удалить студента', 'func': group.deleteStudent},
    {'name': 'Удалить всех студентов', 'func': group.clearStudents},
    {'name': 'Сохранить', 'func': group.saveGroup},
    {'name': 'Завершить работу'}
]


def main():
    while True:
        menu = default_menu if group.name == '' else group_menu
        print('Меню:' if group.name == '' else 'Группа {}:'.format(group.name))
        for i, item in enumerate(menu):
            print(i, '-', item['name'])

        selected_index = MenuInput('Выберите: ')
        print("------------------------------")

        if menu[selected_index]['name'] == 'Завершить работу':
            group.name = ''
            group.clearStudents()
            break

        if len(menu) > selected_index >= 0:
            menu[selected_index]['func']()
        else:
            print('Введите корректный индекс')


if __name__ == '__main__':
    main()
