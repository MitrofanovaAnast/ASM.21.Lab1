import aam2107.st14.lab1.main
import aam2107.st14.lab2.main

MENU = [
		["Lab1", aam2107.st14.lab1.main.main],
		["Lab2", aam2107.st14.lab2.main.main]
]

def menu():
	print("------------------------------")
	for i, item in enumerate(sorted(MENU)):
		print("{0:2}. {1}".format(i, item[0]))
	print("------------------------------")
	return int(input())

class group:
	def f(self):
		try:
			while True:
				sorted(MENU)[menu()][1]()
		except Exception as ex:
			print(ex, "\nbye")
