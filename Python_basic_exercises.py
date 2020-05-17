# from:https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world " \
# so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are":

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


#2. Write a Python program to get the Python version you are using.

import sys
print(sys.version)
print(sys.version_info)


# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime
now = datetime.now()
print(now)

# 4. Write a Python program which accepts the radius of a circle from the
# user and compute the area. Go to the editor
# Sample Output:
# r = 1.1
# Area = 3.8013271108436504

import math

radius = float(input("Radius of a circle: "))

pi = math.pi
area = pi*radius*radius

print("The area of a circle with radius " + str(radius) + " is " + str(area))

#5. Write a Python program which accepts the user's first and
# last name and print them in reverse order with a space between them

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
print(last_name + " " + first_name)

# 6. Write a Python program which accepts a sequence of
# comma-separated numbers from user and generate a list
# and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# sequence will generate a string
sequence = input("Give me a sequence of numbers separated by commas: ")

# split() breaks the string by the specified separator
list = sequence.split(",") 
tuple = tuple(list)
print("List: ",list)
print("Tuple: ",tuple)

# 7. Write a Python program to accept a filename from the user
# and print the extension of that. Go to the editor Sample
# filename : abc.java
# Output : java

file_name = input("What's the file name? ")
file_extension = file_name.split(".")
print(file_extension[-1])

# 8. Write a Python program to display the first and last colors
# from the following list.
colour_list = ["Red","Green","White","Black"]

print(colour_list[0].lower(), colour_list[-1].lower())

# using string formatting operator %s
print("%s %s"%(colour_list[0].lower(), colour_list[-1].lower()))

# using f-strings
first_colour = colour_list[0].lower()
last_colour = colour_list[-1].lower()
print(
    f"{first_colour} "
    f"{last_colour}"
)

# 9. Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
# exam_st_date = (14, 10, 2020)
# Sample Output : The examination will start from : 14 / 10 / 2020

exam_st_date = (14, 10, 2020)

day = int(14)
month = int(10)
year = int(2020)

# using %-formatting
print("%s %d / %d / %d"%('The examination will start from:', 14, 10, 2020))

# using str.format()
print("The examination will start from: " + str(14) + " / " + str(10) + " / " + str(2020))

# using f-Strings
print(
    f"The examination will start from: "
    f"{day} / "
    f"{month} / "
    f"{year}"
      )

# 10. Write a Python program that accepts an integer (n) and
# computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

n = int(input("Give me a number: "))

# # defining n, nn, nnn with strings and then
# # transforming n, nn, nnn in integers to calculate the sum
n1 = str(n)
n2 = n1 + n1
n3 = n1 + n2

print(int(n1) + int(n2) + int(n3))

# 11. Write a Python program to print the documents
# (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

docstring describes what the built-in function does
print(abs.__doc__)

print(all.__doc__)

print(any.__doc__)

print(bin.__doc__)

print(bytearray.__doc__)

12. Write a Python program to print the calendar of a
given month and year.
Note : Use 'calendar' module.

import calendar

# calendar.month(year, month)
# leading zeros in decimal integer liter
# als are not permitted;
# use an 0o prefix for octal integers

may2020 = calendar.month(2020, 0o5)

print(may2020)

#13. Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")

# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2020, 7, 2), (2020, 7, 11)
# Expected output : 9 days

from datetime import date

date1 = date(2020, 7, 2)
date2 = date(2020, 7, 11)

num_dates = date2 - date1

print(date1)
print(date2)

print(num_dates)

# 15. Write a Python program to get the volume of a sphere with radius 6.

# vol = 4/3 x pi x r3

import math
pi = math.pi
r = 6
vol = (4/3) * (pi) * (r*r*r)

print(
    f"The volume of a sphere with radius "
    f"{r} "
    f"is "
    f"{vol}"
)
