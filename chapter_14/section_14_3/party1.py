# Chapter 14 - Object-oriented programming
# 14.3 Using objects

# File: party1.py
# Description - This program creates a list, adds two strings to it,
#               sorts the list alphabetically,
#               and then prints the first element of the sorted list three times
#               using different methods of accessing that element.

# Initialize an empty list named stuff.
stuff = list()
# Append the string python to the stuff list.
stuff.append('python')
# Append the string chuck to the stuff list.
stuff.append('chuck')
# Sort the elements of the stuff list in ascending order.
stuff.sort()
# Print the element at index 0 of the sorted stuff list.
print (stuff[0])
# Print the element at index 0 of the stuff list using the __getitem__ method.
print (stuff.__getitem__(0))
# Print the element at index 0 of the stuff list using the
# list class's __getitem__ method, passing stuff as the instance.
print (list.__getitem__(stuff,0))