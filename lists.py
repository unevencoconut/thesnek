# LISTS ( aka Arrays in other Languages )
# There are four collection data types in the Python programming language:
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered and unindexed. No duplicate members.
    # Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# LISTS
    # A List is a collection which is Ordered and Changeable. Written with Square Brackets

theList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(theList)

# Accessing List Items. Starting at Index of Zero
print(theList[1])

# Negative Indexing, means to begin from the End.
print(theList[-1]) # -1 refers to the last item

# Range Indexes
# When specifying a Range, the return value will be a NEW list with specified items.
theListRange = theList[2:5]
print(theListRange)
print(theList)

# By Leaving out the Start Value, the Range will start at the First Item
print(theList[:4])

# By Leaving out the End Value, the Range will go on to the End of the List
print(theList[2:])

# Specificy Negative Indexes if you want to start from the end of the list
print(theList[-4:-1])

# To Change the Value of a specific item, refer to the index number
theList[1] = "blackcurrant"
print(theList)

# Loop through a List
for x in theList:
    print(x)

# Check if an item is present
if "melon" in theList:
    print("Yes, 'Melon' is in the fruits list")

# List Length
print(len(theList))

# Add Items
# append()
theList.append("jackfruit")
print(theList)

# Add Item to Specified Index
# insert()
theList.insert(1, "blueberry")
print(theList)

# Remove Item
# remote()
theList.remove("blackcurrant")
print(theList)

# Remove Specified Index ( or the Last Item if Index not specified )
theList.pop()
print(theList)

# keyword: del
# Removes the specified Index
del theList[0]
print(theList)

# keyword: del
# Can also delete the List completely
del theList # Will complain with an 'theList' is undefined if you try to print

theListIsBack = ["apple", "banana", "cherry"]
print(theListIsBack)

# clear()
# The clear method empties a list
theListIsBack.clear()
print(theListIsBack) #prints an empty list

# COPY A LIST
    # You cannot copy a list simply by typing list2 = list1, 
    # because: list2 will only be a reference to list1, 
    # and changes made in list1 will automatically also be made in list2

# There are two ways to copy a list
# The First way is
# copy()
listone = ["apple","banana","cherry"]
listoneimposter = listone.copy()
print(listoneimposter)

# The second way
# list()
listoneother = list(listone)
print(listoneother)

# JOINING LISTS
    # There are several ways to join or concatendate two or more lists.

# Joining by Operator
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# Another way is appending all the items from List2 into List1, one by one
for x in list2:
    list1.append(x)

print(list1)

# You can use extend() which purpose is toe add elements from one list to another
# extend()
list1.extend(list2)
print(list1)

# The list() Constructor
# Its possible to make a list, with the list constructor
listWithConstructor = list(("apple","banana","cherry")) #note the double round-brackets
print(listWithConstructor)