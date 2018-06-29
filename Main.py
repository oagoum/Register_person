from RegPerson import RegPerson
import os

class Main:
    r = RegPerson()

    print()
    print("           _______")
    print("           WELCOME")
    print("           -------")

    kjor = True
    while kjor:
        print()
        print("# What do you want to do? #")
        print("_________________________________________________________")
        print("To print a person type p")
        print("To quit type q")
        print("To add a person type a")
        print("To remove a person type r")
        print("To see people count type c")
        print("To see the oldes or the youngest person type oy")
        print("To see if a person is the oldest or the youngest type coy")
        print("To write it to a text file type w")
        print("To read a text file type rf")
        print("To clear the terminal type cln")
        print("To see files in the same folder type fi")
        print("---------------------------------------------------------")

        print()
        inp = input("Answer: ")

        if inp == "p":
            if r._linkedlist.isEmpty():
                print("The person register is empty.")
                print()
            else:
                inpP = input("Id for the person: ")
                r._linkedlist.printPerson(inpP)
                print()
        elif inp == "q":
            kjor = False
        elif inp == "cln":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif inp == "fi":
            os.system('dir' if os.name == 'nt' else 'ls')
        elif inp == "a":
            inpA1 = input("Name: ")
            inpA2 = input("Surname: ")
            inpA3 = input("Age: ")

            if inpA1 == "" or inpA2 == "" or inpA3 == "":
                print("Failed, you must have name, surname and age!")
            else:
                print("added person with id " + str(r.add(inpA1, inpA2, inpA3)) + ".")
                print()
        elif inp == "r":
            print()
            inpR = input("Id for the person: ")
            if not r.checkID(inpR):
                print("There is no person in this register, with the ID you have given.")
            else:
                r._linkedlist.removePerson(inpR)
                r.removeID(inpR)
        elif inp == "c":
            print()
            print("Count: " + str(r._linkedlist.nodeCounter()))
        elif inp == "w":
            inpF = input("filename: ")
            r.writeFile(inpF)
        elif inp =="rf":
            inpRF = input("filename: ")
            r.readFile(inpRF)
        elif inp == "oy":
            print("For youngest type y and for oldest type o")
            inpOY = input("Answer: ")

            if r._linkedlist.isEmpty():
                print()
                print("No person in this register.")
            elif inpOY == "y" and r._linkedlist.nodeCounter() == 1:
                print()
                print("There is only one person in this register.")
            elif inpOY == "o" and r._linkedlist.nodeCounter() == 1:
                print()
                print("There is only one person in this register.")
            elif inpOY == "y":
                print()
                print(r._linkedlist._startNode._data.printPerson())
            elif inpOY == "o" and r._linkedlist._endNode is not None:
                print()
                print(r._linkedlist._endNode._data.printPerson())
            else:
                print()
                print("Invalid answer, try again.")
        elif inp == "coy":
            inpCoy = input("Id for the person: ")
            r._linkedlist.checkIfYoungestOrOldest(inpCoy)
        else:
            print()
            print("Invalid answer, try again.")




Main()