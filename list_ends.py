# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last
# elements of the given list. For practice,
# write this code inside a function.

# # for loop without a function
#
# a = [5, 10, 15, 20, 25]
# b = []
#
# b.append(a[0])
# b.append(a[-1])
# print(b)

# inside of a function

def list_ends(a = [5, 10, 15, 20, 25]):
    b = []

    for x in a:
        b.append(a[0])
        b.append(a[-1])
        print(b)
        return

list_ends()

# alternative solution 

a = [5, 10, 15, 20, 25]

def list_ends(x):
    return [x[0], x[-1]]

print(list_ends(a))



