from asm2104.st03.student import Student
from asm2104.st03.Student_VUC import Student_VUC
from asm2104.st03.StrategyFileIO import StrategyFileIO
from asm2104.st03.StrategyIO import StrategyIO


class Group:
	cartoteka = []

	def __init__(self, strategyFile : StrategyFileIO , strategyIO : StrategyIO):
		self._strategyIO = strategyIO
		self._strategyFile = strategyFile

	@property
	def strategyIO(self) -> StrategyIO:
		return self._strategyIO

	@property
	def strategyFile(self) -> StrategyFileIO:
		return self._strategyFile

	@strategyIO.setter
	def strategyIO(self, strategy: StrategyIO) ->None:
		self._strategyIO = strategy

	@strategyFile.setter
	def strategyFile(self, strategy: StrategyFileIO) ->None:
		self._strategyFile = strategy

	def addStudent(self):
		case = int(input(f" ВУЦ : 1 , Не ВУЦ : 0 \n"))
		person = Student_VUC() if case else Student()
		print(person)
		self.fill_in_console(person = person)
		self.cartoteka.append(person)


	def fill_in_console(self, person):
		self._strategyIO.enter(person)

	def print_cartoteka(self):   #распечатает всех из картотеки
		self._strategyIO.printout(self.cartoteka)

	def cartoteka_from_file(self): #загрузит с файла в картотеку
		self.cartoteka = self._strategyFile.input()

	def cartoteka_in_file(self): #выгрузит картотеку в файл
		self._strategyFile.output(self.cartoteka)

	def clear_kartoteka(self):
		del self.cartoteka[:]

	def cartoteka_edit_person(self):
		index = int(input(f"Id персонажа(целое положительное): "))
		try:
			person = self.cartoteka[index]
		except IndexError:
			print(f"Такого персонажа нет в картотеке")
		self.fill_in_console(person)




