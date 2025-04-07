# Chapter 14 - Object-oriented programming
# 14.4 Starting with programs

# File: elev.py
# Description - This program converts a US floor number to a non-US floor number
#               by subtracting 1 and then prints the result.

# Prompt the user to enter the US floor number and store it as a string in the 'usf' variable.
usf = input('Enter the US Floor Number: ')
# Convert the string 'usf' to an integer, subtract 1, and store the result in the 'wf' variable.
wf = int(usf) - 1
# Print the non-US floor number along with a descriptive message.
print('Non-US Floor Number is',wf)