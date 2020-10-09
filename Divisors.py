# Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number


num = int(input("Give me a number:\n"))
divisor_list = []

for i in range(1, num + 1):
    if num % i == 0:
        divisor_list.append(i)

print(divisor_list)





























