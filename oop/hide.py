# Сокрытие
'''
Сокрытие - это ограничение доступа к элементам,
с которыми нельзя работать откуда угодно, а только из класса.

Приватным можно сделать то, что мы однажды создали и забыли.
Например, мы создали url и порт для подключения к db через класс,
и понимаем, что если url изменится, то весь код пойдет к чертям.
Поэтому мы ограничиваем к нему доступ. Изменить его можно только
внутри класса, в котором он создается.

Для работы с приватными свойствами внутри класса следует создать
методы, через которые будет проводиться работа.

Как правило, все свойства делаются приватными, а их изменение
или получение их значения происходит через GetSet-овые функции.
'''

class Human:
	__age = None # Private property
	__friends = set() # Private property list

	# Constructor
	def __init__(self,age,friends=set()):
		self.__age = age
		self.__friends = set(friends)

	# Удаление друга
	def DeleteFriend(self,friend):
		if friend in self.__friends:
			self.__friends.remove(friend)
		else:
			return f"This person has not friend \"{friend}\""

	# Добавление друга
	def AddFriend(self,friend):
		self.__friends.add(friend)

	# Получение списка друзей
	def GetFriends(self):
		return self.__friends

	# Получение возраста
	def GetAge(self):
		return self.__age
	
	# Установка возраста
	def SetAge(self, age):
		self.__age = age

if __name__=="__main__":
	h1 = Human(age=21)