#Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.For example, substring_between_letters("apple", "p", "e") should return "pl"

def substring_between_letters(word, start, end):
  if start and end in word: 
    start_position = word.find(start)
    end_position = word.find(end)
    substring = word[start_position + 1:end_position]
    return substring
  else:
    return word

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
print(substring_between_letters("Priscilla", "P", "a"))


