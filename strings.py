# STRINGS
# Since I'm already familiar with strings from other languages,
# I'll just mark items here that catch my eye

# MULTILINE STRINGS
# You can assign a multiline string to a variable by using THREE Quotes
# Single or Double Quotes is ok
# Line Breaks are represented in the same position as the code
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# STRINGS ARE ARRAYS
    # Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
    # However, Python does not have a character data type, a single character is simply a string with a length of 1.
    # Square brackets can be used to access elements of the string.
    # Starting at Zero

a = "Hello, World!"
print(a[1]) # Here, we want to get the E in Hello.

# SLICE
# You can return a range of characters using the Slice Syntax
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, Slice!"
print(b[2:5]) # Here we are Slicing from position 2 through 5, giving us the LLO

# Slick from a Negative Index
b = "Hello, World!"
print(b[-5:-2]) # Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:
# Note: This might be confusing, for clarity, it starts at the end of the string for the Index.
# So End of String, go left ( down ) 5 positions. Then, end of string, go Left ( down ) two positions. Return those.

# LENGTH
# Standard run of the mil length function
a = "Hello, Length!"
print(len(a))

# STRING METHODS, The Juicey Stuff
#----------------------------------------------------------------------

# strip()
# Removes any whitespace from the beginning or the end
a = "     Hello, No White Space!   "
print(a) #without strip
print( a.strip() ) #with strip

# lower()
# Returns the string in Lower Case
a = "HELLO, LOWERCASE"
print(a.lower())

# upper()
# Returns the string in Upper Case
a = "hello, uppercase"
print(a.upper())

# replace()
# Replaces the selected portion of the string, with the new string
a = "Hello, Replace!"
print(a.replace("H", "J"))
print(a.replace("o","ah")) #seems to use the original Variable, the first replace does not seem perminent?

# split()
# Splits the string into Substrings, if it finds instances of the separator
a = "Hello, Split!"
print(a.split(","))

# Checking a String
# To check if a certain phrase or character is present in a string,
# we can use keywords "in" or "not in"
text = "The rain in Span stays mainly in the plain"
x = "ain" in text # Look for a string of AIN in the Text Variable
print(x) # Returns a Boolean of True

x = "ain" not in text # Check if AIN is NOT present in the following string
print(x) # Returns False, because AIN is in the string

# CONCATINATE
# You can use the + Operator
a = "Hello,"
b = "Concatinate!"
c = a + b
print(c)

# To add white space between them
c = a + "  " + b
print(c)

# STRING FORMAT
# You cant combine strings with numbers using the + operator, BUT
# You can use the format() method
age = 36
text = "My name is John, and I am {}"
print(text.format(age))

