# PYTHON OPERATORS
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
    # Arithmetic operators
    # Assignment operators
    # Comparison operators
    # Logical operators
    # Identity operators
    # Membership operators
    # Bitwise operators

#Python Logical Operators
# IMPORTANT DISTINCTION HERE
# In Javascript these Operators were Character Symbols &&, ||, !
# But those are reserved for Bitwise in Python. Be careful!

# and
x = 2
theAnd = x < 5 and x < 10 # Returns True if BOTH statements are True
print(theAnd)

# or
theOr = x < 5 or x < 4 # Returns True if one of the statements is True
print(theOr)

# not
theNot = not(x < 5 and x < 10) # Reverse the result, Returns False if the Results is True
print(theNot)

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # Returns True because z is the same object x
print( x is y) # Returns False because X is not the same object as Y, even if they have the same content
print( x == y) # To demonstrate the different between IS and == this comparison returns True because X is equal to Y

# in
x = ["apple", "banana"]
print("banana" in x) # Returns True because a squence with the value "banana" is in the list

# not in
x = ["apple", "banana"]
print("pineapple" not in x) # Returns True because a sequence with the value of "Pineapple" is not in the List
