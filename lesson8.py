# Demonstration of dictionaries in Python

# Dictionaries are unordered, mutable collections used to store data in key-value pairs.
# Each item in a dictionary is a key:value pair, where keys must be unique and immutable,
# while values can be of any data type.

# Create a dictionary to represent a student's details.
student = {
    "name": "Gilbert Omosa",  # Key: "name", Value: "Gilbert Omosa"
    "reg": 10234408,          # Key: "reg", Value: 10234408
    "age": 22,                # Key: "age", Value: 22
    "gender": "male"          # Key: "gender", Value: "male"
}

print(student)  # Prints the entire dictionary.
print(student.get("name"))  # Access the value associated with the key "name".
print(student.get("age"))  # Access the value associated with the key "age".
print(student.get("gender"))  # Access the value associated with the key "gender".

# Adding a new key-value pair to the dictionary.
student["height"] = 181  # Add a key "height" with value 181.
print(student)  # Prints the updated dictionary.

# Example of a dictionary with mixed data types for values.
vehicle = {
  "brand": "Tesla",               # String value.
  "model": "CyberTruck",          # String value.
  "electric": True,               # Boolean value.
  "year": 2023,                   # Integer value.
  "colors": ["grey", "matte black", "silver"]  # List value.
}

print(vehicle)  # Prints the entire dictionary.
print(vehicle.keys())  # Prints all the keys in the dictionary.
print(vehicle.values())  # Prints all the values in the dictionary.
print(vehicle["brand"])  # Access the value associated with the key "brand".
print(vehicle["colors"])  # Access the value associated with the key "colors".
print(len(vehicle))  # Prints the number of key-value pairs in the dictionary.
print(len(vehicle["colors"]))  # Prints the number of items in the "colors" list.
print(type(vehicle))  # Prints the type of the object (dictionary).

# Note: Dictionaries cannot have two items with the same key.
# If a duplicate key is used, the last value provided for that key will overwrite the previous value.

# Create a dictionary representing a phone with nested dictionary values.
phone = {
    "brand": "Apple",  # Key: "brand", Value: "Apple"
    "model": "iPhone 14 Pro Max",  # This value will be overwritten.
    "model": "iPhone 15 Pro Max",  # The last value for the "model" key will take precedence.
    "color": "Space Black",
    "storage": 256,
    "price": 1099,
    "features": {  # Nested dictionary to represent detailed specifications.
        "display": "6.7-inch Super Retina XDR display",
        "camera": "48MP Main camera, 12MP Ultra Wide, 12MP Telephoto",
        "processor": "A17 Bionic chip",
        "battery": "Up to 29 hours of video playback"
    }
}

print(phone)  # Prints the phone dictionary, including the nested "features" dictionary.


# Demonstration of sets in Python

# Sets are unordered collections of unique items in Python.
# Key characteristics of sets:
# - They are unordered, so items have no defined order and cannot be accessed by index or key.
# - They are mutable, meaning items can be added or removed, but individual items themselves cannot be changed.
# - Sets do not allow duplicate values; duplicates are automatically ignored.

# Create a set of friends.
friends = {"Alfred", "Victor", "Felix", "Esther", "Samuel", "Nick", "Tony", "Richard", "Joe", "Marie"}

print(friends)  # Prints the set. Items may appear in a different order each time due to the unordered nature of sets.

# Sets are unordered and do not support indexing or keys.
# Items in a set cannot be accessed directly using an index or key.

# Adding an item to the set.
friends.add("Yvonne")  # Adds "Yvonne" to the set.
print(friends)  # Prints the updated set.

# Removing items from the set.
friends.remove("Richard")  # Removes "Richard" from the set. Raises an error if the item does not exist.
print(friends)  # Prints the updated set.

friends.discard("Joe")  # Removes "Joe" from the set. Does not raise an error if the item does not exist.
print(friends)  # Prints the updated set.

# Creating a set of animals.
animals = {"dog", "cat", "bird", "fish", "elephant", "lion", "tiger", "bear", "monkey", "giraffe", "lion"}
print(animals)  # Prints the set. Duplicate items (e.g., "lion") will be removed.

# Sets automatically ignore duplicate values.
print(len(animals))  # Prints the number of unique items in the set.
print(type(animals))  # Prints the type of the object (set).

# Set items can be of any data type.
speed = {15, 21, 32, 43, 54}  # A set containing integers.
print(speed)

alive = {True, False}  # A set containing boolean values.
print(alive)

cars = {"Toyota Camry", "Honda Civic", "Ford Mustang", "Tesla Model 3", "BMW X5"}  # A set containing strings.
print(cars)

loan_rates = {3.5, 4.2, 5.1, 6.8, 7.5}  # A set containing float values.
print(loan_rates)

# Sets can contain mixed data types.
information = {"Honda Civic", 54, True, 7.5}  # A set with mixed data types.
print(information)

# Differences between sets and dictionaries:
# - **Sets**: Store only unique values and have no key-value pairs.
# - **Dictionaries**: Store key-value pairs where keys must be unique, but values can be duplicated.
