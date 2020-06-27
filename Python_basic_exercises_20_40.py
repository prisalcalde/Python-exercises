# 21. Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user.

def odd_even():
    number = int(input("Give me a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

odd_even()
