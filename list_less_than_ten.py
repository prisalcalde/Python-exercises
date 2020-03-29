
"""
Write a program that prints out all the elements of the list that are less than 5

1. Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.

2. Write this in one line of Python.

3. Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.
"""

# 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in a:
    if item < 5:
        print(item)

# 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

[print(item) for item in a if item < 5]


# 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Give me a number: "))

b = []

for item in a:
    if num < item:
        b.append(item)

print(b)
