"""
Write a program that uses a for loop.
Each iteration will ask the user to enter a name (x5)
Add the input to the provided list
"""
names = []
for i in range(5):
    name = input("Enter a name to put into the list=> ")
    names.append(name)
print(f"Here's the list of names you have given me: {names}")