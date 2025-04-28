# ---------------------------------------------
# Operators
# ---------------------------------------------
print("Operators")

# ---------------------------------------------
# Arithmetic Operators
# ---------------------------------------------
print("\nArithmetic Operators")

x = 5
y = 2
print("x = " + str(x))
print("y = " + str(y))
print(f"{str(x)} + {str(y)} = " + str(x + y)) # Addition
print(f"{str(x)} - {str(y)} = " + str(x - y)) # Subtraction
print(f"{str(x)} * {str(y)} = " + str(x * y)) # Multiplication
print(f"{str(x)} / {str(y)} = " + str(x / y)) # Division
print(f"{str(x)} % {str(y)} = " + str(x % y)) # Modulus
print(f"{str(x)} ** {str(y)} = " + str(x ** y)) # Exponentiation
print(f"{str(x)} // {str(y)} = " + str(x // y)) # Floor Division

# ---------------------------------------------
# Assignment Operators
# ---------------------------------------------
print("\nAssignment Operators")

x = 5
x += 5
x -= 3
x *= 2
x /= 2
x %= 2
x = 10
x //= 2
x **= 2
x = 5
x &= 6
x |= 3
x ^= 3
x >>= 3
x <<= 2
print(x)


# ---------------------------------------------
# Comparizon Operators
# ---------------------------------------------
print("\nComparizon Operators")

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# ---------------------------------------------
# Logical Operator
# ---------------------------------------------
print("\nLogical Operators")
x = 5
y = 7
z = 10
print(x < 7 and y < z)
print(x > y or z > y)
print(not(x > y or z > y))

# ---------------------------------------------
# Identity Operators
# ---------------------------------------------
print("\nIdentity Operators")

x = ['a','b']
y = ['a','b']
z = x
print( x is y)
print( x is z)
print( y is not z)

# ---------------------------------------------
# Membership Operators
# ---------------------------------------------
print("\nMembership Operators")

x = ['a','b']
y = ['a','d']

print('a' in x)
print('c' not in x)
print(x in y)