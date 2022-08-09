
# Importing the requests and json modules.
import requests
import json


# Making a request to the API and storing the response in the variable `response_API`
response_API = requests.get("http://madlibz.herokuapp.com/api/random")


# Converting the response from the API into a dictionary.
data = response_API.text
parse_json = json.loads(data)


# Assigning the values of the keys in the dictionary to the variables.
title = parse_json['title']
blanks = parse_json['blanks']
values = parse_json['value']


# Printing the title of the madlib.
print(parse_json['title'])

# Creating an empty list.
madlib_solution = []


# This is a for loop that is iterating through the list of blanks and asking the user to input a value
# for each blank.
for i in blanks:
    madlib_solution.append(input(i+": "))


# Creating an empty list.
final_madlib = []


# This is a for loop that is iterating through the list of values and madlib_solution.
for i, j in zip(values, madlib_solution):
    temp_str = i+j
    final_madlib.append(temp_str)


# Joining the list of strings into one string.
final_madlib = ' '.join(final_madlib)


# Printing the final madlib.
print(final_madlib)
