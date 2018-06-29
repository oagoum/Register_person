from Node import Node

class LinkedList:
    def __init__(self):
        self._startNode = None
        self._endNode = None

    """
    Add function which is sorted by age,
    from youngest to the eldest.
    """
    def add(self, personObject):
        node = Node(personObject)

        if (self.isEmpty()):
            self._startNode = node
        elif self._startNode._data.checkAge(node._data) >= 0:
            node._next = self._startNode
            self._startNode._previous = node
            self._startNode = node
        else:
            now = self._startNode
            found = False
            while now._next is not None:
                if now._next._data.checkAge(node._data) >= 0:
                    node._next = now._next
                    now._next = node
                    node._previous = now
                    node._next._previous = node
                    self._endNode = node._next
                    found = True
                    break

                now = now._next

            if not found:
                now._next = node
                node._previous = now
                self._endNode = node

    """
    Counts nodes in the linkedlist.
    """
    def nodeCounter(self):
        sNode = self._startNode
        count = 0

        while sNode is not None:
            count += 1
            sNode = sNode._next

        return count

    """
    Checks if the startNode is None, 
    if it is then the linkedlist is empty. 
    """
    def isEmpty(self):
        if self._startNode is None:
            return True
        return False

    """ 
    Prints out the person objects
    in the linkedlist, by using the person ID.
    """
    def printPerson(self, id):
        if self.isEmpty():
            print()
            print("The person register is empty.")

        iterNode = self._startNode

        printBool = False
        while iterNode is not None:
            if str(iterNode._data._id) == id:
                print()
                print(iterNode._data.printPerson())
                printBool = True
            iterNode = iterNode._next

        if printBool is False:
            print("There is no person in this register, with the ID you have given.")

    """
    Remove a person, by using person ID
    """
    def removePerson(self, id):
        if self.isEmpty():
            print()
            print("The person register is empty.")
        elif str(self._startNode._data._id) == id:
            self._startNode = None
            print()
            print("Person removed.")
        elif self._startNode._next._next == None and str(self._startNode._next._data._id) == id:
            self._startNode._next = None
            print()
            print("Person removed.")
        elif str(self._endNode._data._id) == id:
            self._endNode = self._endNode._previous
            self._endNode._next._previous = None
            self._endNode._next = None

        iterNode = self._startNode

        while iterNode is not None:
            if id == str(iterNode._data._id):
                iterNode._previous._next = iterNode._next
                iterNode._next._previous = iterNode._previous._next
                iterNode._previous = None
                iterNode._next = None
                print()
                print("Person removed.")

            iterNode = iterNode._next

    """
    Check if a person is the youngest
    or the oldest.
    """
    def checkIfYoungestOrOldest(self, id):
        if self.isEmpty():
            print()
            print("The person register is empty.")
        elif self.nodeCounter() == 1:
            print("There is only one person in this register.")
        elif self._startNode is not None and self._endNode is not None and id == str(self._startNode._data._id):
            print()
            print("This person is the youngest.")
        elif self._endNode is not None and id == str(self._endNode._data._id):
            print()
            print("This person is the oldest.")
        else:
            print()
            print("This person is not the youngest or the oldest.")