# CTCI 3.6: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the oldest (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldst animal of that type). They cannot select which specific animal they would like. Create the data structures to to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.

from data_structures.linkedList import List, Node

class Animal:
    def __init__(self, type):
        self.type = type

class Shelter:
    def __init__(self):
        self.queue = List()
        self.oldDog = None
        self.oldCat = None

    def enqueue(self, a:Animal):
        n = self.queue.append(a)
        if self.oldCat == None and n.element.type == 'cat':
            self.oldCat = n
        elif self.oldDog == None and n.element.type == 'dog':
            self.oldDog = n
    
    def dequeueAny(self) -> Animal:
        if self.queue.count() == 0:
            return None
        
        pet:Animal = self.queue.head.element
        if pet.type == 'dog':
            self.updateOldPointer(self.queue.head)
        else:
            self.updateOldPointer(self.queue.head)
        self.queue.removeNode(self.queue.head)
        
        return pet
    
    def updateOldPointer(self, node:Node):
        next = node.next

        while next != None:
            if next.element.type == 'cat' and node.element.type == 'cat':
                self.oldCat = next
                pass
            elif next.element.type == 'dog' and node.element.type == 'dog':
                self.oldDog = next
                pass

            next = next.next
    
    def dequeueCat(self) -> Animal:
        if self.queue.count() == 0:
            return None
        pet = self.oldCat
        self.updateOldPointer(pet)
        self.queue.removeNode(pet)

        return pet.element
        
    def dequeueDog(self) -> Animal:
        if self.queue.count() == 0:
            return None
        
        pet = self.oldDog
        self.updateOldPointer(pet)
        self.queue.removeNode(pet)
        
        return pet.element