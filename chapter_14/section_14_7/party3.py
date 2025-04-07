# Chapter 14 - Object-oriented programming
# 14.7 Classes as types

# File: party3.py
# # Description - This program defines a class called PartyAnimal with an instance variable x
#                 initialized to 0 and a method party that increments x and prints its current value.
#                 It then creates an instance of PartyAnimal and prints the type of the instance,
#                 the directory of its attributes and methods, the type of the x variable,
#                 and the type of the party method. Essentially, it demonstrates how to inspect the type
#                 and attributes of an object in Python.

# Define a class named PartyAnimal
class PartyAnimal:

    # Define the constructor method __init__ for the PartyAnimal class
    def __init__(self):
        # Initialize an instance variable x to 0
        self.x = 0

    # Define a method named party for the PartyAnimal class
    def party(self) :
        # Increment the instance variable x by 1
        self.x = self.x + 1
        # Print the current value of x
        print("So far",self.x)

# Create an instance of the PartyAnimal class and assign it to the variable an
an = PartyAnimal()
# Print the type of the variable an (which is an instance of the PartyAnimal class)
print ("Type", type(an))
# Print the list of attributes and methods associated with the instance an
print ("Dir ", dir(an))
# Print the type of the instance variable x (which is an integer)
print ("Type", type(an.x))
# Print the type of the instance method party (which is a method object)
print ("Type", type(an.party))



