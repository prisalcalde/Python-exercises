# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
# to largest) and another number. The function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
#
# Extras:
# Use binary search.

def check_number(list, number):
    if number in list:
        return True
    else:
        return False


print(check_number([4, 6, 8, 9, 15, 25, 78, 90], 8))
print(check_number([4, 6, 8, 9, 15, 25, 78, 90], 257))
