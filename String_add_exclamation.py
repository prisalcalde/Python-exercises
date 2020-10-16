# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  new_word = word
  i = len(word)
  if i >= 20:
    return word
  else:
    while i < 20:
      new_word += "!"
      i += 1
    return new_word    
    

print(add_exclamation("October"))
print(add_exclamation("The winter is coming."))
