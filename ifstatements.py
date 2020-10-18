# IF STATEMENTS
# The major difference here, is IDENTATION defines SCOPE
# This might take some adjusting...

a = 33
b = 200

if b > a:
    print("b is greater than a")

# Keyword: elif
# If the previous conditions were not true, then try this condition
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


# Keyword: else
# For all that is not caught, do this
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Shorthand IF Statement
# If you only have on statement to execute, you can put it on the same line.
if a > b: print("a is greater than b")

# Shofthand IF Else ( aka Ternary Operator )
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")

# NESTED IF STATEMENTS
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# PASS STATEMENT
# if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.
# ... this seems ... bad practice maybe?
a = 33
b = 200

if b > a:
    pass