# STRINGS
# Since I'm already familiar with Booleans from other languages,
# I'll just mark items here that catch my eye

# bool()
# The bool() function allows you to evaluate any value, and give you True or False in return.
print( bool("Hello") ) # A String returns True
print( bool(15) ) #A Int returns True

x = "Hello"
y = 15
print(bool(x)) # Returns True
print(bool(y)) # Returns True

# Most Values Are True
# Any String is True, except Empty Ones
# Any Number is True, except 0
# Any List, Tuple, Set, and Dictionary are True, except Empty Ones

disbefale = None # Keyword Value None, used to define a Null Variable
print(bool(disbefale))

# Functions can return a Boolean
def myFunction():
    return True

print(myFunction())