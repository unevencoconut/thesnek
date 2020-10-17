# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

# GETTING A DATA TYPE
# aka How to figure out what the data type of an Object is...
# you'll need the type() function
# type()

x = 5
print( type(x) )

# In Python, the data type is set when you assign a Value to a Variable
aString = "Hello World!"
aInt = 20
aFloat = 20.5
aComplex = 1j
aList = ["apple", "banana", "cherry"] # otherwise known as an Array in JS
aTuple = ("apple", "banana", "cherry")
aRange = range(6)
aDict = {"name": "John", "age": 36}
aSet = {"apple", "banana", "cherry"}
aFrozenSet = frozenset({"apple", "banana", "cherry"})
aBool = True # Bool is case sensitive!
aBytes = b"Hello"
aByteArray = bytearray(5)
aMemoryView = memoryview(bytes(5))

# If you want to specific the fata type, you can set is using a constructor
aString = str("Hello World!")
aInt = int(20)
aFloat = float(20.5)
aComplex = complex(1j)
aList = list(["apple", "banana", "cherry"]) # otherwise known as an Array in JS
aTuple = tuple(("apple", "banana", "cherry"))
aRange = range(6) # LOL, I guess range doesnt change
aDict = dict({"name": "John", "age": 36})
aSet = set({"apple", "banana", "cherry"})
aFrozenSet = frozenset({"apple", "banana", "cherry"})
aBool = bool(5) # Interesting, I dunno what this means yet
aBytes = bytes(5) #Big difference here
aByteArray = bytearray(5) # no change
aMemoryView = memoryview(bytes(5)) # no change