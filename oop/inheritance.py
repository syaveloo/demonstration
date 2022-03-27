# Наследование
'''
Наследование - это использование свойств меньшего класса в большем.

Допустим есть класс Человек. Есть класс Работник. Работник - это
все тот же человек, но он обладает доп. свойствами. И вместо того,
чтобы по-новому задавать свойства для каждого более крупного
класса, мы можем заставить класс унаследовать их от своего родителя.
Родитель - это тот класс, у которого новый класс берет свойства.
'''

class Person:
	# Properties
	__name1 = None
	__name2 = None
	__age = None

	# Constructor
	def __init__(self, name1, name2, age):
		self.__name1 = name1
		self.__name2 = name2
		self.__age = age


	def SetName1(self, name1):
		self.__name1 = name1

	def GetName1(self):
		return self.__name1


	def SetName2(self,name2):
		self.__name2 = name2

	def GetName2(self):
		return self.__name2


	def SetAge(self,age):
		self.__age = age

	def GetAge(self):
		return self.__age

class Employee(Person):
	__inn = None
	__number = None
	__snils = None

	def __init__(self, name1, name2, age, inn, number, snils):
		# super - выполнение функции в род. классе
		super().__init__(name1,name2,age) # Выполнение init в род. классе
		self.__inn = inn
		self.__number = number
		self.__snils = snils

	def GetInn(self):
		return self.__inn

if __name__ == '__main__':
	pass