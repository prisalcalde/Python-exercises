# Ask the user for a number and determine whether the number is
# prime or not. (For those who have forgotten, a prime number is
# a number that has no divisors.). You can (and should!) use your
# answer to Exercise 4 to help you. Take this opportunity to
# practice using functions, described below.

# defining the function to verify if a number is prime
def check_primality(num=int(input("Give me a number: "))):

    # list of divisors of num
    divisor_list = [i for i in range(1, num + 1) if num % i == 0]

    if divisor_list == [1, num]:
        print(str(num) + " is prime!")
    else:
        print(str(num) + " is NOT prime!")
    return

check_primality()


# # 1. previous exercise to find the divisors of a number
#
# num = int(input("Give me a number: "))
# divisor_list = []
#
# for i in range(1, num + 1):
#     if num % i == 0:
#         divisor_list.append(i)
#
# print(divisor_list)
#
# # 2. transforming into a divisors function and calling it
#
# def list_of_divisors():
#
#     num = int(input("Give me a number: "))
#     divisor_list = []
#
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisor_list.append(i)
#
#     print(divisor_list)
#
# list_of_divisors()

# # 3. divisors function using list comprehension
#
# def list_of_divisors():
#
#     num = int(input("Give me a number: "))
#
#     divisor_list = [i for i in range(1, num + 1) if num % i == 0]
#
#     print(divisor_list)
#
# list_of_divisors()


# # 4. divisors function using list comprehension and a default argument

# def list_of_divisors(num=int(input("Give me a number: "))):

#     divisor_list = [i for i in range(1, num + 1) if num % i == 0]
#     print(divisor_list)
#     return divisor_list

# # defining the function to verify if a number is prime
# def check_primality(num=int(input("Give me a number: "))):

#     # calling the function while defining a list variable
#     divisor_list = list_of_divisors()

#     if divisor_list == [1, num]:
#         print("Your number " + str(num) + " is prime!")
#     else:
#         print("Your number " + str(num) + " is not prime!")
#     return 

# check_primality()

