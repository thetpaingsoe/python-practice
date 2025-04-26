# ---------------------------------------------
# Data Types
# ---------------------------------------------
print("Data Types")

# ---------------------------------------------
# String
# ---------------------------------------------
x = "String"
print('"String" is ' + type(x).__name__)

# ---------------------------------------------
# Integer
# ---------------------------------------------
x = 20
print("20 is " + type(x).__name__)

# ---------------------------------------------
# Float
# ---------------------------------------------
x = 20.1
print("20.1 is " + type(x).__name__)

# ---------------------------------------------
# List
# ---------------------------------------------
x = [1, 2, 3]
print("[1, 2, 3] is " + type(x).__name__)

# ---------------------------------------------
# Tuple
# ---------------------------------------------
x = (1, 2, 3)
print("(1, 2, 3) is " + type(x).__name__)

# ---------------------------------------------
# Range
# ---------------------------------------------
x = range(4)
print("range(4) is " + type(x).__name__)
# Range is a special type of object in Python
# that generates numbers on demand, rather than storing them in memory.
# This is useful for large ranges of numbers.
# E.g 
for i in x:
    print(i, end=" ") # output: 0 1 2 3    
print("\n")
# Or you can range like between like this
x = range(5, 10)
for i in x:
    print(i, end=" ") # output: 5 6 7 8 9
print("\n")

# ---------------------------------------------
# Dictionary
# ---------------------------------------------
x = {"name": "Theo", "age": 20}
print("{'name': 'Theo', 'age': 20} is " + type(x).__name__)

# ---------------------------------------------
# Set
# ---------------------------------------------
x = {"Theo", "Leon"}
print("{'Theo', 'Leon'} is " + type(x).__name__)

# ---------------------------------------------
# Frozenset
# ---------------------------------------------
# one forzenset is a set that is immutable
# you cannot add or remove items from it
x = frozenset({"Theo", "Leon"})
print("frozenset({'Theo', 'Leon'}) is " + type(x).__name__)
try:
    x.add("Theo") # this will raise an error
except AttributeError as e:
    print(e) # TypeError: 'frozenset' object has no attribute 'add'

# ---------------------------------------------
# Boolean
# ---------------------------------------------
x = True
print("True is " + type(x).__name__)

# ---------------------------------------------
# Bytes
# ---------------------------------------------
# It stores binary data and is immutable ( you cannot change the value of a byte )
# str is uncoded text
# bytes is coded text (Raw binary data (0–255))
x = b"Bytes"
print("b'Bytes' is " + type(x).__name__)
# Encode/Decode String as one of the sample usage
y = x.decode("utf-8")
print(y) 
z = y.encode("utf-8")
print(z) 

# ---------------------------------------------
# Bytearray
# ---------------------------------------------
# It is mutable ( you can change the value of a byte )
b = bytearray(b'hello')
print("bytearray(b'hello') is " + type(b).__name__)
b[0]=72
print(b) # output: bytearray(b'Hello')

# ---------------------------------------------
# Memoryview
# ---------------------------------------------
b = bytearray(b'hello')
mv = memoryview(b)
print(mv[0])       # 104 (ASCII for 'h')
mv[0] = 72         # change it to 'H'
print(b)
print(mv[0])       # 72 (ASCII for 'H')

# ---------------------------------------------
# None
# ---------------------------------------------
# It is a special type that represents the absence of a value
x = None
print("None is " + type(x).__name__)
if x is None:
    print("x is None")
else:
    print("x is not None")

