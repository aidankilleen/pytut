countries = ["Ireland", "Portugal", "UK", "France", "Germany"]

class User():

    def __init__(self, id, name, email, active):
        self.id = id
        self.name = name
        self.email = email
        self.active = active

    def __str__(self):
        return f"User Object: {self.name}\n{self.email}\n{self.active}\n{self.id}"



# User
# id
# name
# email
# active

if __name__ == "__main__":

    users = [
        User(1, "Alice", "alice@gmail.com", False), 
        User(2, "Bob", "bob@gmail.com", False),
        User(3, "Carol", "carol@gmail.com", False),
        User(4, "Dan", "dan@gmail.com", True),
        User(5, "Eve", "eve@gmail.com", True),
    ]
   
    list = ["apple", "banana", "avocado", "cherry"]
    newlist = [item for item in list if "a" in item]
    print (list)
    print (newlist)

    # list comprehension
    activeusers = [user for user in users if user.active == True]

    for user in activeusers:
        print (f"{user.name} {user.active}")

    inactiveusers = []

    for user in users:
        if (user.active == False):
            inactiveusers.append(user)

    for user in inactiveusers:
        print (f"{user.name} {user.active}")

    list = [1, 2, 4, 3, 6, 8, 10, 9, 7, 22, 17, 14]

    oddnumbers = []

    for item in list:

        print (f"{item} - {item % 2}")

        if (item % 2 == 1):
            oddnumbers.append(item)

    print (oddnumbers)

    evennumbers = [item for item in list if item % 2 == 0]

    print(evennumbers)





