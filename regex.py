# REGEX ( Regular Expression )
# Is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# https://www.w3schools.com/python/python_regex.asp
# Python has it built in.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

# ---

# Print a list of all matches
# In the order they are found
x = re.findall("ai", txt)
print(x)

# If no match is found, a list is empty
x = re.findall("Portugal", txt)
print(x)

# The search() function searches the string for a match
# and returns a Match Object if there is a match.
# Only the FIRST occurence is returned
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# Split() Function returns a list where the string has been split at each match.
x = re.split("\s", txt)
print(x)

# You can control the number of split occurences by specifiying the maxsplit.
x = re.split("\s", txt, 1)
print(x)

# Sub() replaces the matches with the text of your choice
x = re.sub("\s", "9", txt)
print(x)

# You can control the replacements with the Count Parameter
x = re.sub("\s", "9", txt, 2)
print(x)

# The Macth Object
# An object containing the information about the search and the result
x = re.search("ai", txt)
print(x)

