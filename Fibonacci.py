def fibonacci(n):
  fibs = [0, 1]

  if n <= len(fibs) -1:
    return n

  while n > len(fibs) -1:
    fibs.append(fibs[-1] + fibs[-2])

  return fibs[n]







