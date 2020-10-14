# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

def reverse_word_order():
    phrase = input("Give me a long phrase: ")
    list = phrase.split()
    list.reverse()
    return " ".join(list)


print(reverse_word_order())


#Reverse word:

# def every_other_letter(word):
#   new_word = ''
#   i = 0
#   for i in range(len(word)):
#     if i % 2 == 0:
#       print(i)
#       new_word += word[i]
#   return new_word


# print(every_other_letter('Telephone'))


# alternative solution using range jumping at every second index
def every_other_letter(word):
  new_word = ''
  i = 0
  for i in range(0, len(word), 2):
    # if i % 2 == 0:
    new_word += word[i]
  return new_word

print(every_other_letter('Telephone'))


