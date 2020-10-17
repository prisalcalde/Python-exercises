# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the sum of the values of the dictionary
def sum_values(my_dictionary):
  sum_values = 0
  for item in my_dictionary.values():
    sum_values += item
  return sum_values
  
# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all 
# integer keys and values, as a parameter. This function should return the sum of the values of all even keys.
def sum_even_keys(my_dictionary):
  sum_even_values = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      sum_even_values += my_dictionary[key]
  return sum_even_values
