# Demonstration of tuples in Python

# Tuples are ordered and immutable (cannot be changed after creation) collections of items.
# They are similar to lists but have some key differences:
# - Tuples are immutable, while lists are mutable.
# - Tuples are created using parentheses (), while lists use square brackets [].

# Create a tuple to represent days of the week.
days_of_the_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

print(days_of_the_week)  # Prints the entire tuple.
print(days_of_the_week[1])  # Access the second item (index 1) in the tuple.
print(days_of_the_week[2])  # Access the third item (index 2) in the tuple.

print(len(days_of_the_week))  # Prints the number of items in the tuple.

# Creating a single-item tuple.
people = ("Julie",)  # Note: A comma is required for Python to recognize it as a tuple.
print(people)

# Tuples can contain items of any data type.
tupleString = ("Aurelius", "Brutus", "Caesar")  # A tuple containing strings.
print(tupleString)

tupleInt = (1, 5, 7, 9, 3)  # A tuple containing integers.
print(tupleInt)

tupleBoolean = (True, False, False)  # A tuple containing boolean values.
print(tupleBoolean)

# Tuples can contain mixed data types.
tupleMixed = ("abc", 34, True, 40, "male")  # A tuple with mixed data types.
print(tupleMixed)

# Tuples allow duplicate values.
fruits = ("apple", "banana", "cherry", "apple", "cherry", "pineapple", "orange", "banana")
print(fruits)  # Prints the tuple containing duplicate values.
