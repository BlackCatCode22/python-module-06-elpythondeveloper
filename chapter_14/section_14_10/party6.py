# Chapter 14 - Object-oriented programming
# 14.10 Inheritance

# File: party6.py
# Description - This program demonstrates inheritance by creating a CricketFan class
#               that inherits from a PartyAnimal class (assumed to be defined in a separate party.py file).
#               The CricketFan class adds a points attribute and a six method that
#               increments the points and calls the parent class's party method.
#               The program creates instances of both PartyAnimal and CricketFan, calls their methods,
#               and prints the directory of the CricketFan instance to show its inherited attributes and methods.

# Import the PartyAnimal class from the party.py file
from party import PartyAnimal

# Define a class named CricketFan that inherits from PartyAnimal
class CricketFan(PartyAnimal):

    # Define the constructor method __init__ for the CricketFan class, taking a name as input
    def __init__(self, nam) :
        # Call the constructor of the parent class (PartyAnimal) with the provided name
        super().__init__(nam)
        # Initialize the instance variable points to 0
        self.points = 0

    # Define a method named six for the CricketFan class
    def six(self):
        # Increment the instance variable points by 6
        self.points = self.points + 6
        # Call the party method inherited from the PartyAnimal class
        self.party()
        # Print the name and current points
        print(self.name,"points",self.points)

# Create an instance of the PartyAnimal class named Sally and assign it to the variable s
s = PartyAnimal("Sally")
# Call the party method on the Sally instance
s.party()

# Create an instance of the CricketFan class named Jim and assign it to the variable j
j = CricketFan("Jim")
# Call the party method on the Jim instance (inherited from PartyAnimal)
j.party()
# Call the six method on the Jim instance
j.six()
# Print the list of attributes and methods associated with the instance j
print(dir(j))
