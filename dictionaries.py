# DICTIONARIES
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
# DANGEROUS : This is a JS and PHP Overlap. This will confsued you at least once. Good Luck.

aDictionary = {
    "brand":"Nissan",
    "model":"Skyline",
    "year":1998
}

print(aDictionary)

# Accessing Items
# Access items by referring to its Key Name, inside Square Brackets
x = aDictionary["model"]
print(x)

# get()
# This will also give you the same result as above.
x = aDictionary.get("model")
print(x)

# CHANGE VALUES
aDictionary["year"] = 2002
print(aDictionary)

# Looping through a Dictionary
# A For Loop will return the KEYS of the Dictionary

# Return KEYS
for x in aDictionary:
    print(x)

# Return the VALUES
for x in aDictionary:
    print(aDictionary[x])

# Alternatively, you can use the values method
# values()
for x in aDictionary.values():
    print(x)

# Loop both KEYS and VALUES with the items method
# items()
for x, y in aDictionary.items():
    print(x,y)

# Adding Items to a Dictionary
aDictionary["color"] = "liquid blue"
aDictionary["tires"] = "yoko"
aDictionary["rims"] = "king"
print(aDictionary)

# NESTED DICTIONARIES
# This will create a Dictionary with Three Dictionaries
waifus = {
    "toptier":{
        "name": "emilia",
        "type": "elf"
    },
    "midtier":{
        "name": "rem",
        "type": "demon"
    },
    "bottomtier":{
        "name": "rom",
        "type": "demon"
    },
}

print(waifus)