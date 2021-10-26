from .developer import Developer


class TeamLeader(Developer):
    def __init__(self):
        super(TeamLeader, self).__init__()
        self.annualBonus = input('Введите ежегодную премию\n')

    def __str__(self):
        return super(TeamLeader, self).__str__() + f'Ежегодная премия: {self.annualBonus}'
