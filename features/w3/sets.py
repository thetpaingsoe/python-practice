# ---------------------------------------------
# Python Sets
# ---------------------------------------------
print("\nPython Sets")

fruits = {"apple", "banana", "mango"}
print(fruits)

# - Set Don't have defined order
# - We can't change item after we set
# - Duplicated are not allowed

fruits = {"Apple", "Banana", "Apple"}
print(fruits) # Output : "Banana", "Apple"

# False and 0 are the same value
value = {False, "Another", 1, 0}
print(value) # Output : {False, 1, 'Another'}

# Get the len
print(len(value))

# But You can set anytype of data

# ---------------------------------------------
# Access Sets 
# ---------------------------------------------
print("\nAccess Sets")

fruits = { "apple", "banana", "mango" }
for f in fruits:
    print(f)

# checking the value is exist in set
fruit1 = "apple"
if fruit1 in fruits:
    print("Found : " + fruit1) # will print

fruit2 = "melon"
if fruit2 in fruits:
    print("Found : " + fruit2)
else :
    print("Not Found : " + fruit2) # will print


# ---------------------------------------------
# Add Set
# ---------------------------------------------
print("\nAdd Set")

fruits = {"apple", "banana"}

# add one item
fruits.add("orange")

print(fruits) # {'banana', 'orange', 'apple'}

# add another set use, "update"
fruitsSet2 = {"mango", "melon"}
fruits.update(fruitsSet2)

print(fruits) # {'mango', 'orange', 'apple', 'banana', 'melon'}

# you can use any iterable 
fruitIterable = ["cherry", "kiwi"]
fruits.update(fruitIterable)

print(fruits) # {'apple', 'kiwi', 'cherry', 'melon', 'banana', 'orange', 'mango'}


# ---------------------------------------------
# Remove Set
# ---------------------------------------------
print("\nRemove")

fruits = { "apple", "banana", "kiwi" }

# You have to use remove 
fruits.remove("apple")

print(fruits) # {'banana', 'kiwi'}

# If you use remove and set is not exist, 
# It will show error
try:
    fruits.remove("ABC")
    print(fruits)
except Exception as e:
    print(e)

# But if you use discard, it will not show error
fruits.discard("ABC")
print(fruits)

# Remove randon
fruits = { "apple", "banana", "orange", "kiwi"}
fruits.pop() # it will remove random one
print(fruits) 

# Clear the set
fruits.clear()
print(fruits)

# del will delete completely
del(fruits)
try: 
    print(fruits)
except Exception as e :
    print(e) # name 'fruits' is not defined

# ---------------------------------------------
# Join Set
# ---------------------------------------------
print("\nJoin Set")

# Union
set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3) # {'b', 1, 2, 'a', 3, 'c'}

# can use | instaed of union
set4 = set1 | set2
print(set4) # {'c', 1, 2, 3, 'b', 'a'}

# multiple sets join
set5 = {"Z","Y","X"}
set6 = set1.union(set2, set3, set5)
# Or you can use
# set6 = set1 | set2 | set3 | set5
print(set6) # {1, 2, 3, 'Z', 'c', 'b', 'Y', 'a', 'X'}

# Intersection
# Same will be taken to new set
set1 = { "A", "B", "C" }
set2 = { "Z", "Y", "A"}
set3 = set1.intersection(set2)
print(set3) # {'A'}

# Using & is same with intersection
set4 = set1 & set2
print(set4)

# It will update the set1 instead of return new set
# but still perform intersection that means, only keep 
# those whose include in both set
set1.intersection_update(set2)
print(set1) # {'A'}

# Difference
# it will return the difference only from the frist set
set1 = { "A", "B", "C" }
set2 = { "Z", "Y", "A"}
set3 = set1.difference(set2)
print(set3) # {'B', 'C'}

# "-"" will be the same menaing of difference
set4 = set1 - set2
print(set4) # {'B', 'C'}

# difference_update
set1.difference_update(set2)
print(set1) # {'B', 'C'}


# Symmetric Difference
# It only keep not difference from all set

set1 = { "A", "B", "C" }
set2 = { "Z", "Y", "A"}
set3 = set1.symmetric_difference(set2)
print(set3) # {'Y', 'Z', 'B', 'C' }

# ^ is represent the Symmetric
set4 = set1 ^ set2
print(set4) # {'Y', 'Z', 'B', 'C' }

set1.symmetric_difference_update(set2)
print(set1) # {'Y', 'Z', 'B', 'C' }


