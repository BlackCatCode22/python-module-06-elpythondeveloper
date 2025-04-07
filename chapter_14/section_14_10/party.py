# Chapter 14 - Object-oriented programming
# 14.6 Our first Python object

# File: party2.py
# Description - The PartyAnimal class represents an object that tracks the number of parties it has attended.
#               It initializes a counter x to 0 and provides a party method to increment the counter
#               and print the current count.

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
# Call the party method on the an instance
an.party()
# Call the party method on the an instance again
an.party()
# Call the party method on the an instance a third time
an.party()