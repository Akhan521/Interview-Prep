'''
Problem 1: Villager Class
A class constructor is a special method or function that is used to create and initialize a new object from a class. 
Define the class constructor __init__() for a new class Villager that represents characters in the game Animal Crossing. 
The constructor accepts three required arguments: strings name, species, and catchphrase. The constructor defines four properties for a Villager:

name, a string initialized to the argument name
species, a string initialized to the argument species
catchphrase, a string initialized to the argument catchphrase
furniture, a list initialized to an empty list

Example Usage:
apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)

Output:
Apollo
Eagle
pah
[]
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)