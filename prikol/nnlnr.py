from anytree import Node, RenderTree

def tree():
    c = Node("C:\\")
    system32 = Node("\\System32\\", parent=c)
    for pre, fill, node in RenderTree(c):
        print("%s%s" % (pre,node.name))


# Старт
if __name__ == "__main__":
    tree()



'''
class graph:
    def __init__(self,gdict={}):
        self.gdict = gdict
    
    # Вершины
    def getVertices(self):
        return list(self.gdict.keys())

    # Грани
    def getEdges(self):
        return self.findEdges()
    def findEdges(self):
        edgename = []
        for vertex in self.gdict:
            for nextvertex in self.gdict[vertex]:
                if {vertex, nextvertex} not in edgename:
                    edgename.append({vertex, nextvertex})
        return edgename
if __name__ == "__main__":
    gelements = { 
    "a" : ["b","c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
    }
    newgraph = graph(gelements)
    print(newgraph.getEdges())
'''
