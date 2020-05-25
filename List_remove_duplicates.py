# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.
# *Extras:*
# - Write two different functions to do this - one using a loop and constructing
# a list, and another using sets.
# - Go back and do Exercise 5 using sets, and write the solution for that in a
# different function.

# function using a for loop and returning a list
def list_no_duplicates(a):
    # new empty list to add the items from a without duplication
    b = []
    for item in a:
        if item not in b:
            b.append(item)
    return b


print(list_no_duplicates([3, 5, 6, 7, 7, 7, 5]))
print(list_no_duplicates([3, 5, 6, 7, 7, 7, 5, 89]))
print(list_no_duplicates([-3, 3, 6, -5, 0, 5, 6, 7, 7, 7, 5, 89]))


# # function using a set and returning a list
def list_no_duplicates(a):
    for item in a:
        b = set(a)
        return list(b)


print(list_no_duplicates([3, 5, 6, 7, 7, 7, 5]))
print(list_no_duplicates([3, 5, 6, 7, 7, 7, 5, 89]))
print(list_no_duplicates([-3, 3, 6, -5, 0, 5, 6, 7, 7, 7, 5, 89]))


