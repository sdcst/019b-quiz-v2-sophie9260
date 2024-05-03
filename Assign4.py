#!python3
"""
Billy is inviting people to his party.  He is accepting requests
from his friends, but only wants to send 1 invitation out per
person. He decides to store names in a list, and only add the
ones that are not already there.  Can you help a brother out?

Your program should keep asking the user to enter in a name 
(first and last).  If the name is not on the list, add it,
otherwise say "That name is already on the list".

if the user enters in a blank line, then stop the input.
Sort the list of names (it will be sorted by first name)
and print out all of the names on the list.  Also print out
the number of names on the list so he knows how many 
invitations to send.

This program will require you to incorporate everything we
have learned so far.
"""
peopleList = []
name = "sophie"
while name != '':
    name  =  input("Enter the first and last name of the person you wish to add=> ")
    if name in peopleList:
        print("This person is already in the invited list.")
    elif name not in peopleList:
        peopleList.append(name)
else:
    peopleList.sort()
    print(peopleList)
    x = len(peopleList)
    print(f"There will be {x} invited people.")