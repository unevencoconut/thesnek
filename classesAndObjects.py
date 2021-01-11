# Class and Objects
# A Class is an Object Constructor or a "blueprint" if you will.

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:

class Person:
    # SELF can be named anything. It just has to be the first parameter of any function in the class.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Create a Method for the Person Class
    def mymethod(self):
        print("Hello, my name is " + self.name)

# Create new Object with the Person Class
p2 = Person("John", 36)

# Access Object Properties
print(p2.name)
print(p2.age)

# Access Object Method
p2.mymethod()

# Modify Object Properties
p2.age = 40
print(p2.age)

# You can Delete Objects by using the del Keyword
# Here is P1
print(p1)

# Here we delete P1
del p1

# If you now print P1, it will say its not defined.
# print(p1)