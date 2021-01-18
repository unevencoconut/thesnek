# MODULES
# Consider a Module to be the same as a Code Library
# A File containing a set of Functions you want to include.
# This file uses the Modules_Modulefile.py for the examples.

# Standard Module Import
import modules_modulefile

# Create Alias for Module
import modules_modulefile as mm

# When using a Function from a Module, use the syntax: module_name.function_name
modules_modulefile.greeting("Johnathan Joestar")

# Modules can also have Variables of all types
x = modules_modulefile.person1["stand"]
print(x)

# Use Module Alias
y = mm.person1["firstname"]
print(y)

# Python has built in Modues, you can import whenever you like.
import platform
z = platform.system()
print(z)

# You can list all the Function Names or Variable Names in a Module.
# With the dir() function
zz = dir(platform)
print(zz)

# You can choose to import only perts from a Module, using the from Keyword
from modules_modulefile import person2

# When importing using the from Keyword, do not use the Module name when
# referring to elements in the Module. Use it like regular.
print(person2["stand"])