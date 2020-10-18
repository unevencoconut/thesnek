# SETS
# A Set is a collection which is unordered and unindexed.
# In Python, sets are written with curly brackets.
# Special Note: You're probably gonna at least confused this once with the JS Object Shorthand. Good luck.

aSet = {"apple", "banana", "cherry"}
print(aSet) # Sets are Unordered, so you CANT be sure of which order the items appear.

# Since sets are Unorderd, you cannot refer to an Index or a Key
# print(aSet[1]) wont work

# But you can Loop them
for x in aSet:
    print(x)

# You can ask if something is present
print("banana" in aSet)

# You CANT CHANGE a Set
# But you can ADD items.
aSet.add("orange")
print(aSet)

# update()
# This will add more than one item to a set
aSet.update(["orange","mango","grapes"]) # Note the Square Brackets
print(aSet)

# REMOVING ITEMS

# remove()
# This will remove an item, but if it does not exist it will RAISE AN ERROR
aSet.remove("banana")

# discard()
# This will remove an item, but if it doesnt exist it will NOT raise an error
aSet.discard("banana") # Oberve, Banana was removed above, yet no error.

# pop()
# You can use pop, as it will remove the Last Item, but since a set is unordered
# You WONT KNOW, what item gets removed.

x = aSet.pop()
print(x)
print(aSet)


# JOIN TWO SETS
# More than one way
# Special Note: Both union() and update() will exclusde any duplicate items

# union()
# union method returns a NEW SET containing all items from both sets

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# update()
# update method inserts all items from one set into another
set1.update(set2)
print(set1)

