"""
num_holidays = input("How many days of holiday do you have per year? ")

num_holidays = int(num_holidays)

num = num_holidays % 2 #num is the remainder of num_holidays / 2

num = int(num)

#if the remainder is zero, it's an even number, otherwise, it's odd

if num == 0:
    print("It's an even number, enjoy it :)")
else:
    print("That's odd. The number of days of holidays you have is an odd number!")

"""

num_quarantine = input("How many days do you think we'll be in quarantine because of the coronavirus?\n ")

num_quarantine = int(num_quarantine)

num = num_quarantine % 2 #num is the remainder of num_quarantine / 2

num = int(num)

num_four = num_quarantine % 4 #num is the remainder of num_quarantine / 4

num_four = int(num_four)

#if the remainder num is zero, it's an even number, otherwise, it's odd

#if the remainder num_four is zero, it's an even number, otherwise, it's odd

if num == 0 and num_four == 0:
    print("That's an even number multiple of 4!")
elif num == 0:
    print("That's an even number...")
else:
    print("That's an odd number!")

num2 = input("\nNow, give me another number:\n ")

num2 = int(num2)

num3 = input("\nAlright, last number now and we are done:\n ")

num3= int(num3)

if num2 % num3 == 0:
    print("Your second number divided by the third one is even")
else:
    print("Your second number divided by the third one is an odd number")
