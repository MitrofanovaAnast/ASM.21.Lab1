from .user import user

class student(user):
    def __init__(self):
        user.__init__(self)
        self.group=''
        self.course=int()

    def __str__(self):
        result=super().__str__()
        result+=f'Group: {self.group}\n' \
                f'Course: {self.course}\n'
        return result