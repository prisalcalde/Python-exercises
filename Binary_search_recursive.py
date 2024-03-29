def binary_search(sorted_list, target):
  # base cases
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx

  # recursive steps
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  if mid_val < target:
    right_half = sorted_list[mid_idx + 1:]
    # runs binary search on the remaining list on the right of the mid_val excluding the mid_val
    result = binary_search(sorted_list[mid_idx + 1:], target)
    if result == 'value not found':
      return result
    else:
      return result + (mid_idx + 1)


# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))
print(binary_search(sorted_values, 3))
