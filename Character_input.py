# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old

name = input("What is your name? ")
age = int(input("How old are you? "))
year_100 = str((100 - age) + 2020)

print(name + " you will be 100 in " + year_100)
