from .student import Student


class Headmen(Student):
    def __init__(self, f_name='', l_name='', age=None, scholarship=None):
        super().__init__(f_name, l_name, age, )
        self.scholarship = scholarship

    def __str__(self):
        return f"Пользователя зовут {self.first_name} {self.last_name} Этому пользователю {self.age} лет. Статус этого пользователя: староста."