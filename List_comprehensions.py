# Let’s say I give you a list saved in a variable:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes
# a new list that has only the even elements of this list in it.

# for loop to detect even elements

# 1. Detect which elements of a are even
# 2. Create an empty list variable
# 3. Add the even elements to the list
# 4. Write all the above in one line (list comprehension)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for i in a:
    if i % 2 == 0:
        b.append(i)

print(b)

# using list comprehension

b = [i for i in a if i % 2 == 0]

print(b)


