def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  while left_pointer < right_pointer:
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      right_pointer = mid_idx
    if target > mid_val:
      left_pointer = mid_idx + 1
  
  return "Value not in list"

# test cases
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))


# Pointers are indices stored in a variable that mark the beginning and end of a list
# vehicles = ["car", "jet", "camel", "boat"]
# start_of_list = 0
# end_of_list = len(vehicles)
# # 4

# vehicles[start_of_list : end_of_list]
# # ["car", "jet", "camel", "boat"]

# middle_of_list = len(vehicles) // 2
# # 2

# vehicles[start_of_list : middle_of_list]
# # ["car", "jet"]

# vehicles[middle_of_list : end_of_list]
# # ["camel", "boat"]
