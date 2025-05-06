# ---------------------------------------------
# Tuplies
# ---------------------------------------------
print("Tuplies")

# Tuple are ordered, unchangable and allow duplicate values
tuples = ('apple', 'banana', 'cherry')
print(tuples)

# len of tuple
print(len(tuples))

# Inorder to be tuples, you must have at least with one comma
x = ('apple',)
y = ('apple')
print(type(x)) # tuple
print(type(y)) # str

# it's possible to create tuple with constructor
z = tuple(('apple', 123, True))
print(z)

# ---------------------------------------------
# Access Tuple Items
# ---------------------------------------------
print("\nAccess Tuple Items")

# it can use both positive and nagative indexing.
x = ('apple', 'banana', 'cherry', 'mango', 'orange')
print(x[0]) # apple
print(x[-1]) # orange

# Range of indexes
print(x[2:4]) # cherry, mango

# with nagative index
print(x[-4:-2]) # banana, cherry

# Check item exist
if 'apple' in x:
    print("Apple is in the tuple")

# ---------------------------------------------
# Change Tuple Items
# ---------------------------------------------
print("\nChange Tuple Items")

# Tuple are unchangable, so you cannot change, add or remove items
# but, you can convert tuple to list, change it and convert back to tuple
x = ('apple', 'banana', 'cherry', 'mango', 'orange')
x = list(x)
x[1] = 'kiwi'
x = tuple(x)
print(x)
print(type(x))

# Add tuple to tuple
x = ('apple', 'banana')
y = ('cherry',)
x += y
print(x)

# Remove tuple
x = ('apple', 'banana', 'cherry')
y = list(x)
y.remove('banana')
x = tuple(y)
print(x)

# ---------------------------------------------
# Unpacking Tuple
# ---------------------------------------------
print("\nUnpacking Tuple")

x = ('apple', 'banana', 'cherry')
a, b, c = x
print(a)
print(b)
print(c)

# Unpack as list using *
x = ('apple', 'banana', 'cherry', 'mango', 'orange')
a, b, *c = x
print(a)
print(b)
print(c)

a, *b, c = x
print(a)
print(b)
print(c)

# ---------------------------------------------
# Loop Tuple
# ---------------------------------------------
print("\nLoop Tuple")

x = ('apple', 'banana', 'cherry')
for val in x:
    print(val)

# Loop with range
for i in range(len(x)):
    print(x[i])

# while loop
i = 0
while i < len(x):
    print(x[i])
    i += 1

# ---------------------------------------------
# Join Tuple
# ---------------------------------------------
print("\nJoin Tuple")

x = ('apple', 'banana', 'cherry')
y = ('orange', 'kiwi', 'melon')
z = x + y
print(z)

k = x * 2
print(k)

# ---------------------------------------------
# Methods
# ---------------------------------------------
print("\nMethods")

x = ('apple', 'banana', 'cherry', 'apple')
print(x.count('apple'))
print(x.index('banana'))


