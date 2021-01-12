# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Child Class | First Example
class Student(Person):
    pass # Use pass, when you do not want to add any other properties or methods

# The Child has now inherited the Person Class
y = Student("Mike", "Olsen")
y.printname()

# Child Class | Second Example
class Delinquent(Person):
    def __init__(self, fname, lname): # <- When doing this, you OVERRIDE, the Parents Init Function
        self.firstname = fname
        self.lastname = lname

# To keep the Parent Inheritance, you want to call the Parents Init
class Rockstar(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) # This now properly inherits the Parents Init Function

# But you can go one step furthur and use the Super() Function
class Goldenchild(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) # Super will automatically inherit the methods and properties from the parent.
        self.graduationyear = year # Now we can add additional property and parameter
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)

z = Goldenchild("Ken", "Watanabe", 2020)
z.welcome()

# Woot, I know inheritance.