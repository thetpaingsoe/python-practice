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

# ---------------------------------------------
# Add List Items
# ---------------------------------------------
print("\nAdd List Items")

x = ['apple', 'banana', 'kiwi']
x.append('mango')
print(x)

# extend
x = ['a', 'b', 'c']
y = ['y', 'z']
x.extend(y)
print(x)

# insert
x.insert(3, "x")
print(x)

# ---------------------------------------------
# Remove List Items
# ---------------------------------------------
print("\nRemove List Item")

# Remove
x = ['a','b','c','e']
x.remove('e')
print(x)

# Remove occurence
# It will remove only the first one
x = ['a', 'b', 'a', 'c']
x.remove('a')
print(x)

# Remove with index
x.pop(1)
print(x)

# Remove last index
x.pop() 
print(x)

# Remove with `del` keyword
x = ['a', 'b', 'c', 'd']
del x[1]
print(x)

del x
try:
    print(x)
except NameError as e:
    print(e)

# clear
x = ['a', 'b', 'c']
x.clear()
print(x)

# ---------------------------------------------
# Loop List
# ---------------------------------------------
print("\nLoop List")

x = ['a','b','c']
for val in x:
    print(val)

# with index
print("loop with index")
for i in range(len(x)):
    print(x[i])

# while loop
print("while loop")
i = 0
while i < len(x):
    print(x[i])
    i += 1

# short hand loop
print("Short Loop ")
[print(val) for val in x]

# ---------------------------------------------
# List Comprehension 
# ---------------------------------------------

# From this 
x = ['apple', 'banana', 'orange', 'kiwi']
y = []
for val in x :
    if "a" in val : 
        y.append(val)

print(y)

# With List Comprehension
z = [val for val in x if "a" in val]
print(y)

# Iterable
print("Iterable")
xx = [zz for zz in range(10) ]
print(xx)

# Expression
print("expression")
result1 = [ val.upper() for val in x ]
print(result1)

# Return the item if it is not banana, if it is banana return orange"
result2 = [ val if val != "banana" else "orange" for val in x ]
print(result2)


# ---------------------------------------------
# Sort Lists
# ---------------------------------------------
print("\nSort Lists")

x = ['orange', 'kiwi', 'banana', 'apple', 'watermelon']
x.sort()
print(x)

# reverse
x.sort(reverse = True)
print(x)

# Case senstiitve 
y = ['Orange', 'Kiwi', 'banana', 'Apple', 'melon']
y.sort()
print(y)
y.sort(key = str.lower)
print(y)

# Reverse 
# it is position swap, not based on the value
y.reverse()
print(y)

# ---------------------------------------------
# Copy List
# ---------------------------------------------
print("\nCopy List")
x = ['a', 'b', 'c']
y = x
x.append('d')
print(x)
print(y)

z = x.copy()
x.append('e')
print(x)
print(z)

a = list(x)
x.append('f')
print(x)
print(a)

b = x[:]
x.append('g')
print(x)
print(b)

# ---------------------------------------------
# Join List
# ---------------------------------------------
print("\nJoin List")

x = ['a','b','c']
y = ['d','e','f']

# with +
a = x + y
print(a)

# loop and append
z = x.copy()
for val in y :
    z.append(val)
print(z)

# using extend
x.extend(y)
print(x)

# ---------------------------------------------
# Multi-Dimentional Matrix
# ---------------------------------------------
print("\nMatrix ")
matrix = [
    [2,5,3,9],
    [4,3,2,3],
    [1,4,3,6],
    [3,1,8,2],
]
for row in matrix :
    print(row)

print("\n after sorted first row")
matrix[0].reverse()
for row in matrix :
    print(row)

print("\n Column 2 array")
colIndex = 2
col = [row[colIndex] for row in matrix]
print(col)
col.reverse()
print(col)

print("\n Column 2 Rversed")
for index, row in enumerate(matrix) : 
    row[colIndex] = col[index]

for row in matrix :
    print(row)

arr = [2,3,5]
arr[1] += 1

print(i)

# r = arr.array(2)
# print(r)
# # arr[5] += 1

# print(arr)


def flippingMatrix(matrix):
    dimension = len(matrix)  # This is 2N
    N = dimension // 2       # This is N
    print(f"d : {dimension}, N : {N}")
    max_total_sum = 0

    # Iterate through the rows of the TOP-LEFT N x N quadrant
    for r in range(N):
        # Iterate through the columns of the TOP-LEFT N x N quadrant
        for c in range(N):
            # Get the four symmetric values for the current (r, c) slot
            print(f"r : {r} , c : {c}")
            # 1. Top-Left quadrant element itself
            val1 = matrix[r][c]
            print(val1)
            # 2. Top-Right quadrant symmetric element
            # Same row 'r', but column mirrored from the end
            print(f"r : {r} , c : {dimension - 1 - c}")
            val2 = matrix[r][dimension - 1 - c]
            print(val2)
            # 3. Bottom-Left quadrant symmetric element
            # Row mirrored from the end, same column 'c'
            print(f"r : {dimension - 1 - r} , c : {c}")
            val3 = matrix[dimension - 1 - r][c]
            print(val3)
            # 4. Bottom-Right quadrant symmetric element
            # Both row and column mirrored from the end
            print(f"r : {dimension - 1 - r} , c : {dimension - 1 - c}")
            val4 = matrix[dimension - 1 - r][dimension - 1 - c]
            print(val4)

            print('\n')
            # Choose the largest among these four and add to the sum
            max_total_sum += max(val1, val2, val3, val4)

    return max_total_sum

# Test with your example:
my_matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49], 
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]

result = flippingMatrix(my_matrix)
print(f"The maximum possible sum for the top-left quadrant is: {result}") # Expected: 26


a = [ 'o', 'l', 'm', 'k', 'n' ]
a.sort()
print(a)