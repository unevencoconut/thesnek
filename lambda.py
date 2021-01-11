# LAMBDA
    # A Lambda Function is a Small Anonymouse Function
    # A Lambda can take any number of Arguments,
    # But can only have one Expression
    # Use Lambda Functions whan an Anon Func is required for short period of time.

# Syntax
# lambda argument : expression

# Simple Example
x = lambda a : a + 10
print(x(5))

# Multi Argument Example
x = lambda a, b : a* b
print(x(5, 6))

# The Power of a Lambda is when its used inside a function

# Example
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
    return lambda a : a * n

# Put the Function in a Variable with the Functions Argument
mydoubler = myfunc(2) # This is N
# Then that Variable allows an argument that goes to the Lamba
print(mydoubler(11)) # This is A

mytripler = myfunc(3)
print(mytripler(11))
