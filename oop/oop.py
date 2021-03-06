# Объектно-ориентированный подход
'''
Класс - Описание объекта
Объект - Пример того, что попадает под описание класса

Свойства класса - Признаки, которыми описываются его экземпляры
Методы класса - Действия, которые может совершать объект. Ходить, умирать.

Получение экземпляра класса должна быть в каждом классе,
в ней обычно присваиваются значения для экземпляра.
'''

class Rectangle:
    w = None # Свойство
    h = None # Свойство
    
    # Получение экземпляра класса
    def __init__(self, width, height):
        self.w = width
        self.h = height
    
    # Метод
    def calcArea(self):
        return self.w * self.h


if __name__ == '__main__':
    figure1 = Rectangle(5,5)
    print(figure1.calcArea())