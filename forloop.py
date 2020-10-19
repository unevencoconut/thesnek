#PYTHON FOR LOOP
    # A for loop is used for iterating over a sequence 
    # (that is either a list, a tuple, a dictionary, a set, or a string).
# Special Note: This is less like the for keyword in other programming languages, 
# and works more like an iterator method as found in other object-orientated programming languages.

# LOOP THROUGH STRING
    # Strings are Iterable Objects, they container a sequence of Characters
for x in "banana":
    print(x)

# BREAK STATEMENT
    # Can stop the Loop before it has Looped all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) # Observe, Break after the Print
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        break
    print(x) # Observe, break Before the Print

# CONTINUE STATEMENT
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range()
    # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
    # and ends at a specified number.

for x in range(6):
    print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3): #Increment the sequence with 3
    print(x)

# Keyword: Else
# Specifies a Block of Code to be executed when the Loop is finished
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# NESTED LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)