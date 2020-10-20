# LAMBDA
    # A Lambda Function is a Small Anonymouse Function
    # A Lambda can take any number of Arguments,
    # But can only have one Expression

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

mydoubler = myfunc(2) # Wait ... why does this work?
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))