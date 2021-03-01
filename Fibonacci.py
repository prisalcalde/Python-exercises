# def fibonacci(n):
#   fibs = [0, 1]

#   if n <= len(fibs) -1:
#     return n

#   while n > len(fibs) -1:
#     fibs.append(fibs[-1] + fibs[-2])

#   return fibs[n]

def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  
  fibs = [0, 1]
  if n <= len(fibs) -1:
    return n
  for i in range(2, n+1):
    fibs.append(fibs[i -1] + fibs[i - 2])
  return fibs[n]


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]   

# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)
