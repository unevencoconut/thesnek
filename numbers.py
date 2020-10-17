#NUMBER TYPES
# Three Number Types
    # int
    # float
    # complex

x = 1 # int
y = 2.8 # float
z = 1j # complex

print(x,y,z)

# INT
# These are WHOLE numbers, positive or negative, without decimals, of unlimited length
x = 1
y = 483029543278463287
z = -478342986

print(x,y,z)

# Float ( Floating Point Number )
# A number, positive or negative, containing one more more decimals
x = 1.10
y = 1.0
z = -35.59

print(x,y,z)

# Floats can also be Scientific Numbers with an "e" to indicate the power of 10
x = 35e3
y = 12e4
z = -87.7e100

print(x,y,z)

# COMPLEX
# Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(x,y,z)

# TYPE CONVERSION
# You can convert from one type to another with the methods int(), float(), complex()

x = 1
y = 2.8
z = 1j

#convert from int to float
a = float(x)
print(a)

#convert from float to int
b = int(y)
print(b)

#convert from int to comlex
c = complex(x)
print(c)

# Special Note!
# You cannot convert Complex Numbers into another number type

# RANDOM NUMBER
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1,10))