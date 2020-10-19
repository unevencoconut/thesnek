# FUNCTIONS
    # A Function is defined using the "def" keyword

# Creating a Function
def my_function():
    print("Hello, World! but with a Function, OoOo")

# Calling the created Function
my_function()

# Arguments ( aka args )
    # Parameters: A variable listed inside the parentheses in the Function Definition
    # Argument: A value that is sent to the Function when it is called
# By Default, a Function must be called with the correct number of Arguments.
# If you have two Arguments, then you must use two arguments.
def nameFunction(fname):
    print(fname + " Refsnes")

nameFunction("Emil")
nameFunction("Tobias")
nameFunction("Linus")

# ARBITRART ARGUMENTS ( aka *args )
    # If you do not know how many arguments will be passed into your Function,
    # add a "*" before the Parameter Name in the Function Definition.
    # This will then make the function receive a Tuple of Arguments.

def arbitraryArguments(*idunno):
    print("Everything passed here will be arbitrary! Stuff like " + idunno[2]) #Prints the ROM, being the second index.

arbitraryArguments("Emilia", "Rem", "Rom")

# KEYWORD ARGUMENTS ( aka kwargs)
    # You can send arguments with Key Value Syntax.
    # This way, the order of arguments does not matter.

def keywordArguments(waifu3, waifu2, waifu1):
    print("The top Waifu would be " + waifu3 )

keywordArguments(waifu1="Rom",waifu2="Rem",waifu3="Emilia")

# ARBITRARY KEYWORD ARGUMENTS (aka **kwargs )
    # If you do not know how many Keyword Arguments will be passed, use two asterisk.
    # This created a DICTIONARY of Arguments

def arbitKeywordArgs(**waifu):
    print("Keepin the top spot is " + waifu["therealone"])

arbitKeywordArgs(thefavorite="Rem", therealone="Emilia", thebro="Rom" )

# Default Parameter Value
def defaultParameter(topspot = "Emilia"):
    print("Who is the Top Spot? " + topspot)

defaultParameter("Maybe Rem")
defaultParameter()

# PASSING A LIST AS AN ARGUMENT
    # You can send any data types of argument to a function (string, number, list, dictionary etc.), 
    # and it will be treated as the same data type inside the function.

def passingList(food):
    for x in food:
        print(x)

fruitlist = ["apple", "banana", "cherry"]
passingList(fruitlist)

# RETURN VALUE
    # To let a function Return a Value, use the return statement

def returnDis(x):
    return 5 * x

print(returnDis(3))
print(returnDis(5))
print(returnDis(7))

# RECURSION
    # This means a Function can call ITSELF
    # CAUTION: This can make an infinite function call

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(3)