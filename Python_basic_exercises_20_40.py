  
# from:https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 21. Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user.

def odd_even():
    number = int(input("Give me a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

odd_even()

# 22. Write a Python program to count the number 4 in a given list.

def count_fours(given_list):
    count = 0
    for item in given_list:
        if item == 4:
            count += 1
    return count


count_fours([5, 6, 3, 4, 4, 4, 7, 4, 5, 6])
count_fours([4, 4, 4, 4, 4])
count_fours([])

# 23. Write a Python program to get the n (non-negative integer)
# copies of the first 2 characters of a given string. Return the n
# copies of the whole string if the length is less than 2.

def get_n_first_two_characters(n, given_string):

    if len(given_string) < 2:
        return n*given_string
    else:
        first_two_characters = given_string[0] + given_string[1]
        return n*first_two_characters


print(get_n_first_two_characters(3, "tea"))
print(get_n_first_two_characters(78, "t"))

# 24. Write a Python program to test whether a passed letter is a vowel or not.

import string

def vowel_check(passed_letter):
    if passed_letter in string.ascii_lowercase:
        print("Is vowel")
    else:
        print("Not vowel")

vowel_check("k")
vowel_check("K")
