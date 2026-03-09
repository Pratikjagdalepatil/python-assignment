# Creating an empty set
numbers1 = set()
#print(type(numbers1))

# Creating a set with elements
numbers2 = {5, 10, 15, 20}

# Accessing elements using loop
print("Elements in numbers2:")
for value in numbers2:
    print(value)

# Another collection
numbers3 = (10, 25, 30, 5)

# Adding a new element
#numbers2.add(35)
#print("numbers2:", numbers2)

# Union of sets
union_result = numbers2.union(numbers3)
#print("Union:", union_result)

# Intersection of sets
intersection_result = numbers2.intersection(numbers3)
#print("Intersection:", intersection_result)

# Length of the set
#print("Length of numbers2:", len(numbers2))

# Difference of sets
difference_result = numbers2.difference(numbers3)
#print("Difference (numbers2 - numbers3):", difference_result)
