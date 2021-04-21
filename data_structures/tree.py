class Tree:    
    def __init__(self, value):
        self.rootValue = value
        self.children = []
        pass
    
    def addChild(self, value):
        node = Tree(value)
        self.children.append(node)
        return node

    def removeChild(self, node):
        for subChild in node.children:
            self.children.append(subChild)
        self.children.remove(node)

        pass

    def getChildren(self):
        return self.children

    def countNodes(self):
        sum = 1
        for child in self.getChildren():
            sum = sum + child.countNodes()

        return sum

    def depth(self):
        if len(self.children) == 0 :
            return 1

        max = 0
        for child in self.children:
            depth = 1 + child.depth()
            if  depth > max:
                max = depth
        
        return max


    def __str__(self) -> str:
        s = self.rootValue
        s = str(s)+ '\n'
        for child in self.children:
            print(child.rootValue)
            s = s+child.__str__()
        
        return s



    