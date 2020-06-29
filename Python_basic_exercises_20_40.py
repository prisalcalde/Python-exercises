  
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
