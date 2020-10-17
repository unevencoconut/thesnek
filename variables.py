# Variables
    # Variables are created when you assign a value to it
    # They do not need to be declared with any particular TYPE
    # They can even be changed after they have been set
    # DIFFERENCE: Python has NO COMMAND for Declaring a Variable
# Variable Rules:
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
x = 5 # This is a type of INT
y = "Hello, World!" # Here is a string
print(x,y,"then string")

x = "Its no longer five" # This now changes the X variable above
print(x)

singleQuoteString = 'Single Quote String Is Ok'
doubleQuoteString = "Double Quote String Is OK"
print(singleQuoteString)
print(doubleQuoteString)

#Multiple Variables in one line
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Same value to multiple variables
x = y = z = "Ornanry"
print(x)
print(y)
print(z)

#Output Variables
#Cobining both text and variable, Python uses the + Character
x = "awesome"
print("Python is " + x)

#You can also use the + Character to add variables to another variables
x = "Bruh python really is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
z = x + y
print(z)

#You can't combine string and number, Python will error
#This will produce an error
# x = 5
# y = "John"
# print(x + y)

#Global Variables
#Global variables can be used by everyone, both inside of functions and outside
x = "This be a Global Variable"

def myfunc():
    print("What be dis? " + x)

myfunc()

#Local Variable
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "Dis be Global Too"
def myfunctwo():
    x = "But dis be sneaky local variables"
    print("Who be dis imposter? " + x)

myfunctwo()

print("I be the tru true Global")

#Global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def myfuncthree():
    global x
    x = "What was once local, now be global"

myfuncthree()

print("Come into the light, " + x)

#Changing a Global from within a Function

x = "I be global and unchanged!"
def myfuncfour():
    global x
    x = "But not anymore, a local has changed you!"

myfuncfour()

print("The world is spinning, now what happened? " + x)

# That be all there is to be about Variable Basics. WOOT