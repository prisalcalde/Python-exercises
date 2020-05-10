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
