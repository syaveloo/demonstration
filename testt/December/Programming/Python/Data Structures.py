def integer():
    integer = int(1)
    print("Integer - Целое число")
    print(integer + 5, integer-5, integer*5, integer/5, integer**5)
    print(integer.bit_length())
    print(bin(integer))

def floatnum():
    floatnum = float(1.01)
    print("Float - Число с плавающей точкой")
    print(floatnum-0.02, floatnum-0.01, floatnum*20, floatnum**3)

def string():
    string = str("String")
    print("String - Строка текста, последовательность символов юникода")
    print("\u0430", "a", "| Нет разницы на вид, но первый символ - юникод, второй - с клавиатуры")

def boolean():
    amitrue = bool(False)
    print("Bool - Тип данных, имеющих значение 0 или 1 (False | True).")
    print(2>1, 2<1)

def tuplefunc():
    antuple = tuple((1,2,55,1))
    print("Tuple - Неизменяемый список")

    try:
        antuple[0] = 0
    except Exception as e:
        print(e)
    
    print(antuple[2])

def setfunc():
    anset = set({"apple", "banana", "cherry"})
    print("Set - Список, доступ только через цикл for")

    for x in anset:
        print(x)
    
    anset.add("mishutka")
    print(anset)

    anset.remove("mishutka")
    print(anset)

def dictfunc():
    andict = dict({"key1": 1, "key2":2, "key1": 4})
    print("Dictionary - Словарь структуры 'key: value'.")
    print(andict)
    print(andict["key1"])
    
    andict["key2"] = 4
    print(andict)

    andict["key3"] = None
    print(andict)

    andict.pop("key1")
    print(andict)

    print(andict.get("key2"))

    print(andict.setdefault("key1","value"))
    print(andict)
    print(andict.setdefault("key1","value2"))
    print(andict)

    andict2 = andict.copy()
    print(andict2)

    andict2.clear()
    print(andict2)

def listfunc():
    anlist = list([1,0,4,1])
    print("List - Тип данных для хранения любого колва любых объектов")
    anlist.append("append")
    print(anlist)

    anlist.insert(0,"insert")
    print(anlist)

    anlist.remove(1)
    print(anlist)

    print(anlist.pop(1))
    print(anlist)

    # 0,3 - start,end positions
    print(anlist.index(4,0,3))

    print(anlist.count(1))

    anlist.reverse()
    print(anlist)

    anlist2 = anlist.copy()
    print(anlist2)

    anlist2.clear()
    print(anlist2)

def linkedlist():
    class Node:
        def __init__(self, dataval=None):
            self.dataval = dataval
            self.nextval = None

    class SLinkedList:
        def __init__(self):
            self.headval = None

        def listprint(self):
            printval = self.headval
            while printval is not None:
                print (printval.dataval)
                printval = printval.nextval

    list = SLinkedList()
    list.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    # Link first Node to second node
    list.headval.nextval = e2

    # Link second Node to third node
    e2.nextval = e3

    list.listprint()

if __name__ == "__main__":
    linkedlist()
    