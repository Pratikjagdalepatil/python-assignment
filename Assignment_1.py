# We Can Create Lists Of : Str, Float, Int

marks = [83, 62, 49, 59, 93]
foods = ["Kachori", "Pizza", "Gulabjamun", "Pasta"]

# Printing A Lists
print(marks)
print(foods)

# Printing Length
print(len(marks))
print(len(foods))

# Indexing (Printing Position)
print(marks[3])
print(foods[2])
# Indexing In Lists

# a b c d e f g h i j
# 0 1 2 3 4 5 6 7 8 9

marks = [72, 58, 97, 78, 64]
print(marks)

# Changing Something
marks[2] = 83
print(marks)

# Printing max value
print(max(marks))

# Printing min Value
print(min(marks))
list = [2, 1, 3]

# Reverses the list

list.reverse()
print(list)

# Inserting at any position

list.insert(2,4)
print(list)

# Deleting any value

list.remove(4)
print(list)

# Add Element to end

list.append(4)
print(list)

# Delet any index

list.pop(3)
print(list)

# Sort in Ascending Order

list.sort()
print(list)

# Sort in Descending Order

list.sort(reverse=True)
print(list)
# Slicing In List

foods = ["Samosa", "Burger", "Vadapav", "Pizza"]

print(foods)
print(foods[1:3])
print(foods[:4])
print(foods[1:])