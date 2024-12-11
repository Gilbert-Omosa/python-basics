# Demonstration of lists in Python

# Lists are ordered collections of items that can store multiple values.
# They are mutable, meaning their contents can be changed.

# Create a list of scores.
scores = [90, 56, 45, 69, 29, 93, 44, 87, 68, 23, 67]

# Accessing values in a list using indices.
print(scores[0])  # Prints the first value in the list (index 0).
print(scores[2])  # Prints the third value in the list (index 2).
print(scores[-1])  # Prints the last value in the list using a negative index.

# Adding a value to the list.
scores.append(80)  # Adds the value 80 to the end of the list.
print(scores)  # Prints the updated list.

# Removing a value from the list.
scores.pop(5)  # Removes the value at index 5 (6th position in the list).
print(scores)  # Prints the updated list.

# Sorting the list in descending order.
scores.sort(reverse=True)  # Sorts the list in descending order.
print(scores)  # Prints the sorted list.
