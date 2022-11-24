# countries.py
# By: Aidan
# Date: 24/11/2022

countries = ["Ireland", "Portugal", "UK", "France", "Germany"]


class User():

    def __init__(self, id, name, email, active):
        self.id = id
        self.name = name
        self.email = email
        self.active = active

    def __str__(self):
        return f"User Object: {self.name}\n{self.email}\n{self.active}\n{self.id}"

class Country():
    def __init__(self, name, continent, population):
        self.name = name
        self.continent = continent
        self.population = population