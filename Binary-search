# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
# to largest) and another number. The function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean. Use binary search.

def binary_search(list, number):

    # Ordering the list
    list.sort()
    # print(list)

    # defining the first and last element of the sorted_list (by index)
    first_item_index = 0
    last_item_index = len(list) - 1

    while first_item_index <= last_item_index:
        middle_item_index = last_item_index - first_item_index // 2
        middle_item = list[middle_item_index]

        if middle_item == number:
            #returns the position (index) of the number in the list
            return middle_item_index
        elif number < middle_item:
            last_item_index = middle_item_index - 1
        else:
            first_item_index = middle_item_index + 1
    return False


print(binary_search([2, 4, 6, 8, 44, 77, 90, 360, 450], 360))
print(binary_search([2, 4, 6, 8, 44, 77, 90], 25))
print(binary_search([2, 4, 90, 6, 8, 44, 77, 160, 3, 1, 6, 88, 480], 25))
print(binary_search([2, 4, 90, 6, 8, 44, 77, 160, 3, 1, 6, 88, 480], 480))
