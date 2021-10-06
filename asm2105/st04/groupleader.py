from abc import ABC
from dataclasses import dataclass
from asm2105.st04.member import Member


@dataclass()
class GroupLeader(Member, ABC):
    stipend: int = 4000

    def setData(self):
        super(GroupLeader, self).setData()

    def showData(self):
        super(GroupLeader, self).showData()

    def __str__(self):
        return 'Староста ' + super(GroupLeader, self).__str__()
