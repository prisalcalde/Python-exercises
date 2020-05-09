# Write a program that asks the user how many Fibonnaci numbers
# to generate and then generates them. Take this opportunity
# to think about how you can use functions. Make sure to ask
# the user to enter the number of numbers in the sequence to
# generate.
# (Hint: The Fibonnaci sequence is a sequence of numbers where
# the next number in the sequence is the sum of the previous
# two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fib_gen(n = int(input("How many fibonacci numbers would you like me to generate? "))):
    a = 0
    b = 1

    # will print 0 - the first fibonacci number
    if n == 1:
        print(a)

    # will print 0, 1 and the other fibonacci numbers
    else:
        print(a)
        print(b)

    # 2 is the third position because the first and second are a and b
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

fib_gen()







