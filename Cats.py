class Cat:
  def __init__(self, input_name, input_breed, input_is_cuddly, input_age=0):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = input_is_cuddly
    self.friends = []
  
  def cuddly_cats(self, other_cat):
    if (other_cat.is_cuddly):
      self.friends.append(other_cat)
      print(f"{other_cat.name} is {self.name}'s friend and it loves cuddlying.")
    else:
      print(f"{other_cat.name} doesn't like too much cuddlying.")

  def __repr__(self):
    if len(self.friends) != 1:
      return f"{self.name} is a {self.breed} and it's {self.age} years old. It has {len(self.friends)} friends."
    else:
      return f"{self.name} is a {self.breed} and it's {self.age} years old. It has {len(self.friends)} friend."

cat_zero = Cat("Kitty", "Persian", True, 16)
cat_one = Cat("Kito", "Tabby", False, 2)
cat_two = Cat("Tiko", "Ginger domestic cat", True, 0)

cat_zero.cuddly_cats(cat_one)
cat_one.cuddly_cats(cat_zero)
cat_zero.cuddly_cats(cat_two)
print("....................")
print(cat_zero)
print(cat_one)
print(cat_two)


