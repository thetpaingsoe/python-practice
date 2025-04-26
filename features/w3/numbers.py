# ---------------------------------------------
# Numbers
# ---------------------------------------------
print("Numbers")

# ---------------------------------------------
# Integer
# ---------------------------------------------
print("\nInteger")

x = 1
y = 2323423523235
z = -2323423523235
print(x)
print(y)
print(z)

# ---------------------------------------------
# Float
# ---------------------------------------------
print("\nFloat")

w = -23.0
x = 1.5
y = 1.5e2
z = 1.5e-2
print(w)
print(x)
print(y)    
print(z)

# ---------------------------------------------
# Complex
# ---------------------------------------------
# number with real and imaginary parts
# It is useful in scientific calculations and in engineering
# where complex numbers are used.
# E.g Audio, Radio processing, Fractals, Mandelbrot sets, etc.
print("\nComplex")

x = 1j
y = 2j
z = 3j
print("1j is " + type(x).__name__)
print(x)
print(y)
print(z)

x = 1 + 2j
y = 2 + 3j
print(x + y)
print(abs(x))

# ---------------------------------------------
# Type Casting
# ---------------------------------------------
print("\nType Casting")

x = 1
y = 2.8
z = 3j

a = float(x)
b = int(y)
c = complex(x)

print(a, type(a))
print(b, type(b))
print(c, type(c))

# ---------------------------------------------
# Random Number
# ---------------------------------------------
import random
print("\nRandom Number")

print(random.randint(10, 15), end=" ") # include both ends
