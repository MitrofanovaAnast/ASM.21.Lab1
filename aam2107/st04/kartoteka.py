from .FileIO import FileOutputPickle
from .Employee import Employee
from .Chief import Chief
	

class MenuKartoteka:
	def __init__(self, strategy=FileOutputPickle()):
		self.__cart = []
		self.__strategy = strategy

	def add(self):
		case = int(input("0 - Работник, 1  - Начальник: \n"))
		employee = Chief() if case else Employee()
		employee.input()
		self.__cart.append(student)

	def change(self):
		index = int(input("Введите номер работника (начиная с 1)"))
		self.__cart[index-1].input()

	def print(self):
		for st in self.__cart:
			st.output()

	def file_read(self):
		self.__cart = self.__strategy.do_input()

	def file_write(self):
		self.__strategy.do_output(self.__cart)

	def clear(self):
		self.__cart.clear()

