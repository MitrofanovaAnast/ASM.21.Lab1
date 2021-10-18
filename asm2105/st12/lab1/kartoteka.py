if __name__ == '__main__':
	from ConsoleIO import ConsoleIO as CI
	from FileIO import FileOutputPickle, FileOutputShelve
	from Stusent import Student as St
	from Captain import Captain as Cap
else:
	from .ConsoleIO import ConsoleIO as CI
	from .FileIO import FileOutputPickle, FileOutputShelve
	from .Stusent import Student as St
	from .Captain import Captain as Cap
	


class MenuCartoteka:
	def __init__(self, strategy=FileOutputPickle()):
		self.__cart = []
		self.__strategy = strategy

	def add(self):
		case = int(input("0 - Студент, 1  - Староста: \n"))
		student = Cap() if case else St()
		student.input()
		self.__cart.append(student)

	def change(self):
		index = int(input("Введите номер студента, которого нужно изменить"))
		self.__cart[index-1].input()

	def print(self):
		for st in self.__cart:
			st.output()

	def file_read(self):
		self.__strategy.do_output(self.__cart)

	def file_write(self):
		self.__cart = self.__strategy.do_input()

	def clear(self):
		self.__cart.clear()

