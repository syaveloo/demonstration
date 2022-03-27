class Eljur:
	def __init__(self):
		self.__week = 0
		self.__days = dict()

	def GenerateDays(self):
		self.__days["Monday"] = dict({
			"Lessons": {
				"1": {
					"name": "Biology",
					"homework": "Do test"},
				"2": {
					"name": "Music"},
				"3": {
					"name": "Science",
					"homework": "Do II variant"},
				"4": {
					"name": "Chimestry",
					"homework": "Without homework"},
				"5": {
					"name": "Technology"},
				"6": {
					"name": "Technology"},
				"7": {
					"name": "Geometry"}
				}
			})
		self.__days["Wednesday"] = dict({
			"Lessons": {
				"1": {
					"name": "Algebra",
					"homework": ""},
				"2": {
					"name": "Algebra"},
				"3": {
					"name": "Algebra",
					"homework": "№1711"},
				"4": {
					"name": "Chimestry"},
				"5": {
					"name": "Sport"},
				"6": {
					"name": "Sport",
					"homework": "Make a video about sport"},
				"7": {
					"name": "Geography",
					"homework": "Read §11"}
				}
			})

	def GetDays(self):
		return self.__days

	def GetWeek(self):
		return self.__week

class Week:
	def __init__(self):
		pass



class Lesson:
	def __init__(self, name, homework):
		self.__name = name
		self.__homework = homework

class Day:
	def __init__(self, name, lessons):
		self.__name = name
		self.__lessons = []


if __name__ == "__main__":
	# make stuff
	eljur = Eljur()
	eljur.GenerateDays()

	# get stuff
	days = eljur.GetDays()



