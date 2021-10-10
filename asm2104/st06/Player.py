from asm2104.st06.Member import Member


class Player(Member):
    def __init__(self):
        Member.__init__(self)
        self.country = input('Enter country\n')
        self.position = input('Enter position\n')

    def __str__(self):
        text = super().__str__()
        text += f'Country: {self.country}\n' \
                f'Position: {self.position}\n' \
                f'Member Type: Player'
        return text
