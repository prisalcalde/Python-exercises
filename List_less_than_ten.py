# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)

# ----------------------------------------
# Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it and print out this new list.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i < 5:
        b.append(i)

print(b)

# ----------------------------------------
# Write this in one line of Python

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# b = [i for i in a if i < 5] # using list comprehension
# print(b)

# ----------------------------------------
# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Give me a number:\n"))

c = []

for i in a:
    if i < num:
        c.append(i)

print(c)

# or

num = int(input("Give me a number:\n"))

c = [i for i in a if i < num]

print(c)
