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

# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
# The function should add 10 to every value in my_dictionary and return my_dictionary.
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
# This function should return a list of all values in the dictionary that are also keys.
def values_that_are_keys(my_dictionary):
  list_values = []
  for key in my_dictionary:
    if key in my_dictionary.values():
      list_values.append(key)
  return list_values

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function 
# should return the key associated with the largest value in the dictionary.
def max_key(my_dictionary):
  values_list = []
  for key in my_dictionary:
    values_list.append(my_dictionary[key])
  values_list.sort()
  max_value = values_list[-1]
  for key in my_dictionary:
    if my_dictionary[key] == max_value:
      return key

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
def word_length_dictionary(words):
  words_dictionary = {}
  for item in words:
    words_dictionary[item] = len(item)
  return words_dictionary

# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a 
# dictionary containing the frequency of each element in words.
def frequency_dictionary(words):
  words_dictionary = {}
  for item in words:
    if item not in words_dictionary.keys():
      words_dictionary[item] = 1
    else:
      words_dictionary[item] += 1
  return words_dictionary

# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the 
# number of unique values in the dictionary.
def unique_values(my_dictionary):
  unique_values = []
  for value in my_dictionary.values():
    if value not in unique_values:
      unique_values.append(value)
  return len(unique_values)

#Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where 
# the key is a last name and the value is a list of first names. For example, the dictionary might look like this:
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people 
# whose last name begins with that letter.
# So in example above, the function would return:
# {"S" : 4, "L": 3}


def count_first_letter(names):
  # key - first letter of the last name
  # value - number of people whose last name begines with that letter
  new_dictionary = {}
  for key, value in names.items():
    first_letter = key[0]
    if first_letter not in new_dictionary:
      new_dictionary[first_letter] = 0
    new_dictionary[first_letter] += len(value)  
  return new_dictionary

    
