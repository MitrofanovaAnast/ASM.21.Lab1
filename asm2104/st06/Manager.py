from asm2104.st06.Member import Member


class Manager(Member):
    def __init__(self):
        Member.__init__(self)
        self.role = input('Enter role\n')

    def __str__(self):
        text = super().__str__()
        text += f'Role: {self.role}\n' \
                f'Member Type: Manager'
        return text
