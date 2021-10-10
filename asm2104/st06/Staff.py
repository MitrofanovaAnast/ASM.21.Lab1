from asm2104.st06.Member import Member


class Staff(Member):
    def __init__(self):
        # super(Staff, self).__init__()
        Member.__init__(self)
        self.position = input('Enter position\n')

    def __str__(self):
        text = super().__str__()
        text += f'Position: {self.position}\n' \
                f'Member Type: Staff'
        return text
