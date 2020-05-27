# Write a password generator in Python. Be creative with how you generate passwords.
# Strong passwords have a mix of:
# - lowercase letters
# - uppercase letters
# - numbers
# - symbols
# The passwords should be random, generating new password every time the user
# asks for a new password. Include your run-time code in a main method.
# Extra:
# - Ask the user how strong they want their password to be.
# - For weak passwords, pick a word or two from a list.

# -------------------------------------------------------
# *** Second solution ***
# - Removed the string variables
# - Defined the password variable with the random generators directly (without using a list)
# -------------------------------------------------------

import random
import string

# Function to generate a random 6 character-password
def gen_password():
    password = (str(random.randrange(10))) + random.choice(string.punctuation) + random.choice(string.ascii_lowercase) +random.choice(string.punctuation) + random.choice(string.ascii_uppercase + str(random.randrange(10)))
    print(password)
    return password


gen_password()

# -------------------------------------------------------
# *** First solution (not optmised yet, but works) ***
# -------------------------------------------------------

# Module to generate random stuff
import random

# Module to manipulate strings
import string

# -------------------------------------------------------
# Rules for a 6-character password
# - 2 letters (1 uppercase, 1 lowercase)
# - 2 digits (0 - 9)
# - 2 special characters

# -------------------------------------------------------
# String variables
special_characters = string.punctuation
lowercase_alphabet = string.ascii_lowercase
uppercase_alphabet = string.ascii_uppercase

# -------------------------------------------------------
# Function to generate a random 6 character-password
def gen_password():
    password_list = []
    character_1 = random.randrange(10)
    character_2 = random.randrange(10)
    character_3 = random.choice(uppercase_alphabet)
    character_4 = random.choice(lowercase_alphabet)
    character_5 = random.choice(special_characters)
    character_6 = random.choice(special_characters)

    password_list.append(character_1)
    password_list.append(character_2)
    password_list.append(character_3)
    password_list.append(character_4)
    password_list.append(character_5)
    password_list.append(character_6)

    random.shuffle(password_list)
    password = "".join([str(x) for x in password_list])
    print(password)
    return password


gen_password()

# -------------------------------------------------------
# Function to generate a password after asking the user
# how strong they want their password to be
def gen_password():
    strength = str(input("Would you like a strong, super strong or a weak password? "))

    if strength == "super strong":
        password_list = []
        character_1 = random.randrange(10)
        character_2 = random.randrange(10)
        character_3 = random.choice(uppercase_alphabet)
        character_4 = random.choice(lowercase_alphabet)
        character_5 = random.choice(special_characters)
        character_6 = random.choice(special_characters)
        character_7 = random.randrange(10)
        character_8 = random.randrange(10)
        character_9 = random.choice(uppercase_alphabet)
        character_10 = random.choice(lowercase_alphabet)
        character_11 = random.choice(special_characters)
        character_12 = random.choice(special_characters)

        password_list.append(character_1)
        password_list.append(character_2)
        password_list.append(character_3)
        password_list.append(character_4)
        password_list.append(character_5)
        password_list.append(character_6)
        password_list.append(character_7)
        password_list.append(character_8)
        password_list.append(character_9)
        password_list.append(character_10)
        password_list.append(character_11)
        password_list.append(character_12)

        random.shuffle(password_list)
        password = "".join([str(x) for x in password_list])
        print(password)
        return password

    elif strength == "strong":
        password_list = []
        character_1 = random.randrange(10)
        character_2 = random.randrange(10)
        character_3 = random.choice(uppercase_alphabet)
        character_4 = random.choice(lowercase_alphabet)
        character_5 = random.choice(special_characters)
        character_6 = random.choice(special_characters)

        password_list.append(character_1)
        password_list.append(character_2)
        password_list.append(character_3)
        password_list.append(character_4)
        password_list.append(character_5)
        password_list.append(character_6)

        random.shuffle(password_list)
        password = "".join([str(x) for x in password_list])
        print(password)
        return password

    elif strength == "weak":
        password_list = ["blueberry", "raspberry", "strawberry", "broccolli", "apple", "lettuce"]
        password_list = random.sample(password_list, 2)
        random.shuffle(password_list)
        password = "".join([str(x) for x in password_list])
        print(password)
        return password

    else:
        print("I can only give you 'weak', 'strong' or 'super strong' passwords.")
        return


gen_password()
