# Chapter 14 - Object-oriented programming
# 14.8 Object lifecycle

# File: party4.py
# Description - This program defines a class PartyAnimal that tracks a party count.
#               It includes a constructor to initialize the count and print a construction message,
#               a party method to increment and display the count,
#               and a destructor to print a destruction message with the final count.
#               It then creates an instance, calls the party method twice, and reassigns the variable to an integer,
#               triggering the destructor before the reassignment.

# Define a class named PartyAnimal
class PartyAnimal:

    # Define the constructor method __init__ for the PartyAnimal class
    def __init__(self):
        # Initialize an instance variable x to 0
        self.x = 0
        # Print a message indicating that the object has been constructed
        print('I am constructed')

        # Define a method named party for the PartyAnimal class
    def party(self) :
        # Increment the instance variable x by 1
        self.x = self.x + 1
        # Print the current value of x along with a message
        print('So far',self.x)

        # Define the destructor method __del__ for the PartyAnimal class
    def __del__(self):
        # Print a message indicating that the object is being destructed, along with the final value of x
        print('I am destructed', self.x)

# Create an instance of the PartyAnimal class and assign it to the variable an
an = PartyAnimal()
# Call the party method on the an instance
an.party()
# Call the party method on the an instance again
an.party()
# Reassign the variable an to the integer 42,
# which will trigger the destructor of the PartyAnimal object previously referenced by an.
an = 42
# Print the current value of an (which is now 42)
print('an contains',an)



