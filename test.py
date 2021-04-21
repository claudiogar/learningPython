from algos.quicksort import quicksort
from algos.mergesort import mergesort
from data_structures import tree

def tree_test():
    root = tree.Tree(0)
    child1 = root.addChild(1)
    child2 = child1.addChild(2)
    child3 = child1.addChild(3)
    child4 = child2.addChild(4)
    child5 = child4.addChild(5)
    #    0
    #    1
    #   2  3
    #  4
    #  5
    print(root.countNodes())
    print("depth: "+(str(root.depth())))
    pass


def quicksort_test():
    array = [5,1,4,57,2,4,9,90]
    quicksort(array)

    print(array)
    pass

def mergesort_test():
    array = [5,1,4,57,2,4,9,90]
    array = mergesort(array, 0 , len(array)-1)

    print(array)
    pass

mergesort_test()