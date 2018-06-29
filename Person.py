class Person:
    idI = 0
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        self._id = Person.idI
        Person.idI += 1

    """
    Prints the person informartion
    to the terminal.
    """
    def printPerson(self):
        print()
        print("Name: " + self._name)
        print("Surname: " + self._surname)
        print("Age: " + self._age)

        return ""

    """
    Used to compare age, 
    for the sort function in LinkedList.py. 
    """
    def checkAge(self, person):
        if self._age > person._age:
            return 1
        else:
            return -1