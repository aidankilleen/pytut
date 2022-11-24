# Person.py
# By: Aidan
# Date: 23/09/2022

class Person():

    def __init__(self, name, email):
        # this function gets called int initialise a new object
        # print("__init__ called")
        self.name = name
        self.email = email

    def __str__(self):
        # this function gets called to convert this object to a string
        return f"{self.name} - {self.email}"

    def display(self):
        print (self.name)
        print (self.email)

if __name__ == "__main__":

    #code for testing the module often goes here

    people = [
        Person("Alice", "alice@gmail.com"), 
        Person("Bob", "bob@gmail.com"), 
        Person("Carol", "carol@gmail.com"), 
        Person("Dan", "dan@gmail.com"), 
    ]

    for person in people:
        #person.display()
        print (person)



    #p = Person("Bob", "bob@gmail.com")

    #p.display()

    #print (p.name)
    #print (p.email)


