from random import choice as random
from string import ascii_letters, digits, punctuation

character = digits+ascii_letters+punctuation
length_of_password = int(input("Enter length of password:(Greater than 8 characters!) "))
password = "".join(random(character)for every_character in range(length_of_password))

print(password)