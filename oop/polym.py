class Person:
	__age = None
	def __init__(self,age):
		self.__age = age

	def hello(self):
		print(f"hello im person")

class Employee(Person):
	__age = None
	def __init__(self,age):
		super().__init__(age)

	def hello(self):
		print(f"hello im Employee")

class Proger(Employee):
	__age = None
	def __init__(self,age):
		super().__init__(age)

	def hello(self):
		print(f"hello im Proger")

if __name__ == '__main__':
	for cl in [Person,Employee,Proger]:
		cl(21).hello()