# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

# Lists, Tuples, Dictionaries, and Sets are all Iterable Objects.
# They are Iterable CONTAINERS, which you can get an Iterator from.
# They all have an iter() method

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) # Apple
print(next(myit)) # Banana
print(next(myit)) # Cherry
# If you try to print one more, it errors.

# Strings are also iterable
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# A For Loop, can be used to iterate though an Iterable Object
# The For Loop actually creates an Iterator Object and executes the next() method just like above
for x in mytuple:
    print(x)

# Create An Iterator
# You have to implement the methods __iter__() and __next__()

class MyNumbers:
    # __iter__() method acts similar to the __init__() method.
    # You can do operations with it ( initializing etc )
    # But you must always return the Iterator Object itself.
    def __iter__(self):
        self.a = 1
        return self

    # __next__() method allows you to do Operations
    # It must return the next item in the sequence
    # The example below, will loop FOREVER, if you run a for loop on it.
    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    # So we have to make sure to use StopIteration, to stop is from going forever.
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

# The class above, returns numbers, starting with 1, and each sequence will increase by one.
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)

# Iterations, Done.