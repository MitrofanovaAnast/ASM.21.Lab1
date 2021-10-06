from .console import MenuInput
from .groupleader import GroupLeader
from .member import Member
from dataclasses import dataclass, field
from typing import List
import pickle

from .student import Student

student_types = [
    {'name': 'Студент', 'class': Student},
    {'name': 'Староста', 'class': GroupLeader}
]


@dataclass
class Group:
    name = ''
    group_members: List[Member] = field(default_factory=list)

    def setName(self):
        self.name = input('Введите название группы: ')
        print("------------------------------")

    def addStudent(self):
        for i, item in enumerate(student_types):
            print(i, '-', item['name'])

        selected_index = MenuInput('Выберите тип студента: ')
        print("------------------------------")
        member = student_types[selected_index]['class']()
        member.setData()
        self.group_members.append(member)

    def editStudent(self):
        self.showStudents()
        i = MenuInput('Введите индекс студента: ')
        try:
            user = self.group_members[i]
            user.setData()
            print('Пользователь {} {} отредактирован'.format(user.name, user.second_name))
        except IndexError:
            print('Такого пользователя не существует')

    def deleteStudent(self):
        self.showStudents()
        i = MenuInput('Введите индекс студента: ')
        try:
            cached_name = '{} {}'.format(self.group_members[i].name, self.group_members[i].second_name)
            self.group_members.pop(i)
            print('Пользователь ', cached_name, ' Удален')
        except IndexError:
            print('Такого пользователя не существует')

    def showStudents(self):
        for i, item in enumerate(self.group_members):
            print(i, '- ', end='')
            item.showData()
        print("------------------------------")

    def saveGroup(self):
        with open('asm2105/st04/group.dat', 'wb') as f:
            pickle.dump({'name': self.name, 'data': self.group_members}, f)
        print('Файл успешно сохранен!')

    def loadGroup(self):
        with open('asm2105/st04/group.dat', 'rb') as f:
            tmp = pickle.load(f)
            self.name = tmp['name']
            self.group_members = tmp['data']
        print('Файл успешно загружен!')

    def clearStudents(self):
        self.group_members.clear()
        print('Все пользователи удалены!')
