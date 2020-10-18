# TUPLES
    # A tuple is a collection which is ordered and UNCHANGEABLE
    # Written with Round Brackets

aTuple = ("apple", "banana", "cherry")
print(aTuple)

# Once a Tuple is Created, you cannot add items to it. They are unchangeable.
# aTuple[3] = "orange"
# Will raise an error stating Tuple Object does not support item assignment

# A Tuple with ONE ITEM
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thisIsATuple = ("apple",) # Note the Comma
print(thisIsATuple)

# NOT a Tuple
notATuple = ("apple")
print(type(notATuple)) # Turns out to be a String ... interesting