# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
  return total * (percentage * 0.01) 

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
