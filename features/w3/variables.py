# ---------------------------------------------
# Basic Vairable Declaration
# ---------------------------------------------
print("Variable Declaration")

x = 5
y = "Theo"
print(x)
print(y)

# ---------------------------------------------
# Type Conversion from int to String
# ---------------------------------------------
print("\nType Conversion")

x = 5
x = "String"

print(x)

# ---------------------------------------------
# Casting : If you want to specify the data type
# of a variable, you can use casting.
# ---------------------------------------------
print("\nCasting")

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)    
print(z)

# ---------------------------------------------
# Get the type of variable
# ---------------------------------------------
print("\nType of Variable")

x = 5
y = "5"
print(type(x))
print(type(y))

# ---------------------------------------------
# " and ' are same
# ---------------------------------------------
print("\nDouble and Single Quotes")

x = "Theo"
y = 'Leon'

print(x)
print(y)

# ---------------------------------------------
# Variable names are case-sensitive
# ---------------------------------------------
print("\nVariable Case Sensitivity")

a = 1
A = 2
print(a)
print(A)

# ---------------------------------------------
# Multiple Variables Assignment
# ---------------------------------------------
print("\nMultiple Variables Assignment")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# ---------------------------------------------
# One Value to Multiple Variables
# ---------------------------------------------
print("\nOne Value to Multiple Variables")

x = y = z = "Orange"
print(x)
print(y)
print(z)

# ---------------------------------------------
# Unpacking a Collection
# ---------------------------------------------
print("\nUnpacking a Collection")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# ---------------------------------------------
# Global Variables
# ---------------------------------------------
print("\nGlobal Variables")
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)