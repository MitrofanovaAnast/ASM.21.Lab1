from aam2107.st11.console import Console
from aam2107.st11.file import File


class Pharmacy:
	employeeList = []
	strategy = Console()

	def addEmployee(self):
		self.employeeList.extend(Console().getEmployees())

	def clearEmployees(self):
		self.employeeList.clear()

	def showEmployees(self):
		self.strategy.showEmployees(self.employeeList)

	def getEmployees(self):
		self.employeeList = self.strategy.getEmployees()

	def changeStrategy(self):
		strategy = [
			{'label': 'Консоль', 'class': Console},
			{'label': 'Файл', 'class': File},
		]
		for i in range(len(strategy)):
			print('{0}. {1}'.format(i, strategy[i]['label']))
		try:
			selected = int(input())
			self.strategy = strategy[selected]['class']()
		except:
			print('Введите число от 0 до {}'.format(len(strategy) - 1))
