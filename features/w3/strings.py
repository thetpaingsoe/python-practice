# ---------------------------------------------
# Strings
# ---------------------------------------------
print("Strings")

# ---------------------------------------------
# Quotes inside strings
# ---------------------------------------------
print("\nQuotes")

print("Theo's book")
print('Theo\'s book')
print("He is called 'Theo'")
print('He is called "Theo"')

# ---------------------------------------------
# Multiline strings
# ---------------------------------------------
print("\nMultiline Strings")

x = """This is a multiline string.
It can be used to write long strings
that span multiple lines.
"""
print(x)
y = '''This is a multiline string.
It can be used to write long strings
that span multiple lines.
'''
print(y)

# ---------------------------------------------
# String to Array
# ---------------------------------------------
x = "Hello Theo"
print(x[0]) # H
print(x[6]) # T

# ---------------------------------------------
# Looping strings
# ---------------------------------------------
print("\nLooping Strings")

x = "Hello Theo"
for i in x:
    print(i)

# ---------------------------------------------
# String Length
# ---------------------------------------------
print("\nString Length")

x = "Hello Theo"
y = len(x)
print("Length of " + x + " is " + str(y))

# ---------------------------------------------
# Check String
# ---------------------------------------------
print("\nCheck String")
# You can check a phrase or a character in a string using the keyword "in"
x = "Hello Theo"
print("Based String " + x)
y = "Theo" in x
print("Theo in Hello Theo: " + str(y))
y = "Theo" not in x
print("Theo not in Hello Theo: " + str(y))
z = "T" in x
print("T in Hello Theo: " + str(z))
z = "t" in x
print("t in Hello Theo: " + str(z))

# ---------------------------------------------
# String Slicing
# ---------------------------------------------
print("\nString Slicing")

x = "Hello Theo"
y = x[0:5]
# Slice from the start to the end
print("x[0:5] = " + y) # Hello

# Slice from the start
y = x[:5]
print("x[:5] = " + y) # Hello

# Slice to the end
y = x[6:]
print("x[6:] = " + y) # Theo

# Nagative Indexing
y = x[-4:-1] # reverse indexing starting from -1
print("x[-4:-1] = " + y) # The

# ---------------------------------------------
# Modifying Strings
# ---------------------------------------------
print("\nModifying Strings")

x = "Hello Theo"
print(x.upper()) # HELLO THEO
print(x.lower()) # hello theo
x = " Hello Theo "
print(x) # Hello Theo
# remove whitespace from the beginning and the end
x = x.strip()
print(x) # Hello Theo

# replace string
x = x.replace("Theo", "Leon")
print(x) # Hello Leon

# splict string
x = x.split(" ")
print(x) # ['Hello', 'Leon']

# ---------------------------------------------
# Concact String
# ---------------------------------------------
print("\Concat Strings")

x = "Hello"
y = 'Theo'
print(x + " " + y)

# ---------------------------------------------
# Formatted String
# ---------------------------------------------
print("\nFormatted String")

age = 12
print(f"My name is Theo and I am {age} years old.")

# Add modifiers to the formatted string
price = 23
print(f"This price of this piece is {price:.2f}") # 23.00

# Operations in formatted string
print(f"2 + 3 = { 2 + 3 }") # 2 + 3 = 5

# ---------------------------------------------
# Escape Characters
# ---------------------------------------------
print("\nEscape Characters")

print("Single Quote: \'")
print("Double Quote: \"")
print("Backslash: \\")
print("Tab: \tValue")
print("New Line: \nValue")
print("Backspace: \bValue")
print("Carriage Return: \rValue")
print("Form Feed: \f")
print("Octal: \152")  
print("Hexadecimal: \x48")

