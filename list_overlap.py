# Write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of different sizes

# using set
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i == i in b:
        c.append(i)
        d = list(set(c))

print(d)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# # checking matching numbers and adding to list c
# c = []
# for item in a:
#     if item == item in b:
#         c.append(item)

# # adding only the non duplicate items to list d
# d = []
# for item in c:
#     if item not in d:
#         d.append(item)

# print("New list with matching elements:", str(d))


# generating two random lists to test the code
import random

random_list_a = []
random_list_b = []

random_list_a = random.sample(range(1, 89), 10)
random_list_b = random.sample(range(1, 89), 10)

print("Random list a:" + str(random_list_a))
print("Random list b:" + str(random_list_b))

# checking matching numbers and adding to list random_matching_list
random_matching_list = []
for item in random_list_a:
    if item == item in random_list_b:
        random_matching_list.append(item)

# adding only the non duplicate items to list final_random_matching_list
final_random_matching_list = []
for item in random_matching_list:
    if item not in final_random_matching_list:
        final_random_matching_list.append(item)

print("Final list with matching elements from random lists:", str(final_random_matching_list))



