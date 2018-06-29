from LinkedList import LinkedList
from Person import Person
import os.path

class RegPerson:
    def __init__(self):
        self._linkedlist = LinkedList()
        self._addedID = []

    """
    Used for adding the person object,
    into the linkedlist. 
    """
    def add(self, name, surname, age):
        person = Person(name, surname, age)
        self._addedID.append(person._id)
        self._linkedlist.add(person)

        return person._id

    """
    Checks if the ID is in the person register.
    """
    def checkID(self, idInput):
        for id in self._addedID:
            if str(id) == idInput:
                return True

        return False

    """
    Removes the ID from the addedID array, 
    when removing the person from 
    the doubly linked list in LinkedList.py. 
    """
    def removeID(self, idInput):
        for id in self._addedID:
            if str(id) == idInput:
                self._addedID.remove(id)

    """
    Reads a text file (.txt) and add
    the people to the linkedlist.
    """
    def readFile(self, filename):
        if os.path.isfile(filename + ".txt"):
            with open(filename + ".txt") as file:
                f = file.read(1)
                if not f:
                    print("The file is empty.")
                else:
                    if os.path.isfile(filename + ".txt"):
                        file = open(filename + ".txt", 'r')
                        for person in file:
                            person = person.split(" ")
                            self.add(person[0], person[1], person[2])
        else:
            print("File does not exists.")

    """
    Writes the person objects
    from the linkedlist, to a text file (.txt).
    """
    def writeFile(self, filename):
        file = open(filename+".txt", 'w')

        sNode = self._linkedlist._startNode
        while sNode is not None:
            file.write(sNode._data._name + " " + sNode._data._surname + " " + str(sNode._data._age))
            file.write('\n')
            sNode = sNode._next