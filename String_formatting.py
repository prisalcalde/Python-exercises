# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

def introduction(first_name, last_name):
  return f"{last_name}, {first_name} {last_name}"

  # Other string formatting alternatives: 
  # return last_name + ", " + first_name + " " + last_name
  # return "{last_name}, {first_name} {last_name}".format(last_name = last_name, first_name = first_name)
  # return "%s, %s %s" % (last_name, first_name, last_name)

print(introduction("John", "Lennon"))
# should print Angelou, John Lennon
print(introduction("Priscilla", "Melo"))
# should print Priscilla, Prisclla Melo
