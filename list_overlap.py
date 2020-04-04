# Write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of different sizes

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# checking matching numbers and adding to list c
c = []
for item in a:
    if item == item in b:
        c.append(item)

# adding only the non duplicate items to list d
d = []
for item in c:
    if item not in d:
        d.append(item)

print("The new list is:", str(d))
