# JSON is a syntax for storing and exchanging data.
# JSON is text, written with Javascript Object Notation
# Python has a built-in package for JSON, called json, which is used to work with JSON data.

import json

# If you have a JSON string, you can parse it by using the json.loads() method
# Some JSON:
x = '{"name":"Dio","last":"brando", "age":99, "stand":"da worldo"}'

# pase it
y = json.loads(x)

# the result is a python dictionary
print(y["stand"])

# Convert from Python to JSON
# here is a Python object (dict):
x = {
    "name":"Johnathan",
    "stand":"starplatinum",
    "powerlevel":90000
}

# Convert it into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convert a Python object containing all the legal data types:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# The example above, is not easy to read. You can format it with dumps.
json.dumps(x, indent=4)

# You can also use Separators to change the default separators
json.dumps(x, indent=4, separators=(". ", " = "))

# You can even sort the JSON keys in alphabetical order
json.dumps(x, indent=4, sort_keys=True)