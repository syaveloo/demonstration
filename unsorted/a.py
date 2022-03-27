
def main():
    possible = []
    for x in range(1000,10000):
        y = str(x)
        p1 = int(y[0]) + int(y[1])
        p2 = int(y[2]) + int(y[3])
        print(y)
        print(p1,p2)
        if p1 >= p2:
            possible.append( int(str(p2)+str(p1)) )
        else:
            possible.append( int(str(p1)+str(p2)) )
    return possible

lst = main()
print(lst[-2], type(lst[-2]))
print(1817 in lst)
for x in range(1,1819):
    if x not in lst:
        pass
        #print(x)