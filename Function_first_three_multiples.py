# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

def first_three_multiples(num):
  x = 1
  while x <= 3:
    print(num * x)
    x += 1
  return num * 3

print(first_three_multiples(10))
# should print 10, 20, 30, and return 30
print(first_three_multiples(5))
# should print 5, 10, 15, and return 15
print(first_three_multiples(0))
# should print 0, 0, 0, and return 0
