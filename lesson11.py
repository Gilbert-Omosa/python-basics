# Introduction to functions in Python
import math  # Importing the math module for mathematical operations (e.g., π for circle area)
from datetime import date  # Importing the date module for working with dates

# Function to calculate and print the area of a triangle
def area_of_a_triangle(base, height):
    # Note: Ensure base and height are positive numbers to avoid invalid results.
    area = 0.5 * base * height  # Formula for the area of a triangle
    print(area)  # Print the calculated area

# Function to calculate and print the area of a circle
def area_of_a_circle(radius):
    # Note: Ensure the radius is a non-negative number to avoid invalid results.
    area = math.pi * radius * radius  # Formula for the area of a circle (πr²)
    area = round(area, 3)  # Rounding the area to 3 decimal places for better readability
    print("The area of the circle is", area)  # Print the calculated area

# Function to print the current date
def print_date():
    today = date.today()  # Get the current date
    print(today)  # Print the current date (Format: YYYY-MM-DD)

# Function to calculate and print the total of all numbers passed as arguments
def add(*args):
    # Note: *args allows passing an arbitrary number of arguments to the function.
    total = 0  # Initialize the total to 0
    for number in args:  # Iterate through all arguments
        total += number  # Add each number to the total
    print("The Total is", total)  # Print the total

# Function to print a greeting message with a name and age
def sayHi(name, age):
    # Note: Ensure 'name' is a string and 'age' is a number to avoid errors.
    print("Hello, my name is " + name + ", I am " + str(age) + " years old.")  # Print a formatted message

# Call the functions to demonstrate their functionality

# Calculate and print the area of two triangles
# Note: These examples demonstrate how to pass positional arguments.
area_of_a_triangle(8, 12)
area_of_a_triangle(40, 60)

# Define a list of triangles with base and height values
# Note: Using a list allows batch processing of multiple triangles.
triangles = [[1, 3], [5, 7], [9, 11], [13, 15], [17, 19], [21, 23]]

# Calculate and print the area for each triangle in the list
# Note: Iterating through the list demonstrates the ability to use functions in loops.
for triangle in triangles:
    area_of_a_triangle(triangle[0], triangle[1])

# Calculate and print the area of a circle with a specific radius
# Note: Demonstrates rounding for better presentation of floating-point numbers.
area_of_a_circle(23.45678)

# Print the current date
# Note: Useful for time-sensitive applications.
print_date()

# Calculate and print the total of numbers from 1 to 20
# Note: Passing a large number of arguments showcases the use of *args.
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

# Print a greeting message with a name and age
# Note: Demonstrates combining multiple data types in string formatting.
sayHi("John", 40)
