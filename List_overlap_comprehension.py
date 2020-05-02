# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your
# program works on two lists of different sizes. Write this in one line
# of Python using at least one list comprehension.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# using set comprehension (sets have no duplicates)

c = [i for i in set(a) if i == i in b]

print(c)

# ensuring this work on random lists of different sizes

import random

d = random.sample(range(1, 100), 20)
e = random.sample(range(1, 100), 10)

f = [i for i in set(d) if i in e]

print(d)
print(e)
print(f)
