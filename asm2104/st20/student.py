class Student(object):
    first_name = ''
    last_name = ''
    age = None

    def __init__(self, person_name='', person_surname='', age=None):
        self.first_name = person_name
        self.last_name = person_surname
        self.age = age

    def __str__(self):
        return f"Имя пользователя: {self.first_name} {self.last_name} Этому пользователю {self.age} лет. " \
               f"Статус этого пользователя: студент."
