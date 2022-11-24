#import User
#user = User.User(1, "Alice", "alice@gmail.com", False)
#print (user)


#from User import User
#user = User(2, "Bob", "bob@gmail.com", True)
#print (user)

#from User import *
#user = User(3, "Carol", "carol@gmail.com", True)
#print (user)


from countries import *

user = User(1, "Alice", "alice@gmail.com", True)
print (user)
print (countries)

country_list = [
    Country("Ireland", "Europe", 4500000), 
    Country("Canada", "North America", 100000000), 
    Country("Japan", "Asia", 450000000), 
    Country("Portugal", "Europe", 10000000), 
    Country("UK", "Europe", 650000000), 
    Country("France", "Europe", 1650000000), 
    Country("China", "Asia", 16000000000)
]

europe = [country for country in country_list if country.continent == "Europe"]

for country in europe:
    print (country.name)





