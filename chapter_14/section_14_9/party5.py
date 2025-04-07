# Chapter 14 - Object-oriented programming
# 14.9 Multiple instances

# File: party5.py
# Description - This program defines a PartyAnimal class that tracks the party count for individuals.
#               The class constructor initializes the party count to 0, stores the individual's name,
#               and prints a construction message including the name.
#               The party method increments the count and prints a message with the name and updated count.
#               The program creates two PartyAnimal instances, Sally and Jim,
#               and demonstrates how the party count is tracked separately for each individual.

# Define a class named PartyAnimal
class PartyAnimal:

    # Define the constructor method __init__ for the PartyAnimal class, taking a name as input
    def __init__(self, nam):
        # Initialize the instance variable x (party count) to 0
        self.x = 0
        # Initialize the instance variable name with the provided name
        self.name = nam
        # Print a message indicating the object has been constructed, including the name
        print(self.name,'constructed')

    # Define a method named party for the PartyAnimal class
    def party(self) :
        # Increment the instance variable x (party count) by 1
        self.x = self.x + 1
        # Print a message indicating the name and the current party count
        print(self.name,'party count',self.x)

# Create an instance of the PartyAnimal class named Sally and assign it to the variable s
s = PartyAnimal('Sally')
# Call the party method on the Sally instance
s.party()
# Create an instance of the PartyAnimal class named Jim and assign it to the variable j
j = PartyAnimal('Jim')

# Call the party method on the Jim instance
j.party()
# Call the party method on the Sally instance again
s.party()
