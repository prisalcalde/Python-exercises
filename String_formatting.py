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

# -----------------------------------------------------------

# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. 
# Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"
# Test this function with your name and your age!

def dog_years(name, age):
  age = 7 * age
  return f"{name}, you are {age} years old in dog years"

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
