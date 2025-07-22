# ---------------------------------------------
# Dictionaries
# ---------------------------------------------
print("\nDictionaries")

data = {
    "name" : "Bruno",
    "age" : 30,
    "location" : "England"
}

print(data)
print(data["name"])

# It is changable
data['location'] = "Spain"
print(data)

# But not allow duplicate
data = {
    "name" : "Bruno",
    "name" : "Luna",
    "age" : 30,
    "location" : "England"
}
print(data) # {'name': 'Luna', 'age': 30, 'location': 'England'}

# len
print(len(data)) # 3

# dict constructor
data = dict(name = "john", age = 32)
print(data)


# ---------------------------------------------
# Access Dictionary
# ---------------------------------------------
print("\nAccess")

data = {
    "name" : "John",
    "age" : 22,
    "location" : "Singapore"
}

# get
print(data["name"])
print(data.get("name"))

# Keys
print(data.keys())

# Keys and Changest
data = {
    "name" : "Pink",
    "age" : 25
}

x = data.keys()

print(x) # dict_keys(['name', 'age'])

data['location'] = "Korea"

# x is changing based on the data'keys
print(x) # dict_keys(['name', 'age', 'location'])

# get items
print(data.items())

y = data.items()

print(y) #before the change

data["year"] = 2020

print(y) #after the change

# Check Key is exist
if "year" in data : 
    print("Year is inlucded.")


# ---------------------------------------------
# Change Values
# ---------------------------------------------
print("\nChange Values")

value = {
    "brand" : "ford",
    "year" : 2022,
    "model" : "Mustang"
}

value["year"] = 2020

print(value)

# update 
value.update({"year": 2025})
print(value)

# ---------------------------------------------
# Remove
# ---------------------------------------------

value = {
    "brand" : "ford",
    "year" : 2022,
    "model" : "Mustang"
}

value.pop("model")
print(value) # {'brand': 'ford', 'year': 2022}

# You can use clear, del, popitem like others


# ---------------------------------------------
# Loop
# ---------------------------------------------
print("\nLoop")

values = {
    "brand" : "ford",
    "year" : 2022,
    "model" : "Mustang"
}
print("\nit will print keys")
for val in values :
    print(val)

print("\nkeys")
for key in values.keys():
    print(key)

print("\nvalues")
for val in values.values():
    print(val)

print("\nKey and Values")
for key, value in values.items():
    print(f"key : {key}, value : {value}")


# ---------------------------------------------
# Copy
# ---------------------------------------------
print("\Copy")

values = {
    "brand" : "ford",
    "year" : 2022,
    "model" : "Mustang"
}

# it will create new instance 
copyVal = values.copy()
copyVal2 = dict(values)
print(copyVal)
print(copyVal2)

values['year'] = 1900

print(copyVal)
print(copyVal2)

print(values)

# ---------------------------------------------
# Nested 
# ---------------------------------------------
print("\nNested")

dataDict = {
    "child1" : {
        "name" : "John",
        "num" : 232
    },
    "child2" : {
        "name" : "April",
        "num" : 534
    },
    "child3" : {
        "name" : "Leo",
        "num" : 102
    },
}

print(dataDict)

print(dataDict['child1']['name'])

# Looping
for key, obj in dataDict.items() :
    print(f"key : {key}")
    for key, value in obj.items() : 
        print(f"{key} : {value}")

# add new key
dataDict["child4"] = {
    "name" : "July",
    "num" : 109
}
print("\n")
for key in dataDict.keys() : 
    print(f"key : {key}" )
print(dataDict['child4'])

# remove keys
del dataDict["child2"]
dataDict.pop("child3")

print("\n")
for key in dataDict.keys() : 
    print(f"key : {key}" )