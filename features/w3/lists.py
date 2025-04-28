# ---------------------------------------------
# Lists
# ---------------------------------------------
print("Lists")

x = ['apple','mango','banana']
print(x)
print("List 0 is " + x[0])

# It can have duplicate
x = ['apple','mango','banana', 'apple']
print(x)

#len
print(len(x))

# can have multiple datatype in list
x = ['ABC', 2, False, 23.5]
print(x)

#type
print(type(x))

# list constructor
x = list(('apple','banana'))
print(x)

# ---------------------------------------------
# Access List Items
# ---------------------------------------------
print("\nAccess List Items")
x = ['apple','mango','banana']

# Negative index
print(x[-1])
print(x[-2])

x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Range
print(x[2:5])

# Check item exist
if "apple" in x:
    print("Apple is in the list")

# ---------------------------------------------
# Change List Items
# ---------------------------------------------
print("\Change List Items")

x = ['apple', 'banana', 'cherry', 'orange']
x[1] = 'kiwi'
print(x)

# Change Range
x[1:3] = ['kiwi', 'melon']
print(x)

# If you over add the range it will add as new item
# and the remainig will be shift to end
x[1:2] = ['kiwi', 'mango'] # ['apple', 'kiwi', 'mango', 'melon', 'orange']
print(x)

# If you insert less items than you replace, 
# the new items will be inserted where you specified, 
# and the remaining items will move accordingly:
x[1:4] = ['banana'] # ['apple', 'banana', 'orange']
print(x)

# Insert
x.insert(2, 'cherry')
print(x)