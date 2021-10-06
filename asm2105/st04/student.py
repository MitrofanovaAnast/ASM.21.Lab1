from abc import ABC
from dataclasses import dataclass

from asm2105.st04.member import Member


@dataclass()
class Student(Member, ABC):
    stipend: int = 2000
    
    def setData(self):
        super(Student, self).setData()
        
    def showData(self):
        super(Student, self).showData()

    def __str__(self):
        return 'Студент ' + super(Student, self).__str__()
