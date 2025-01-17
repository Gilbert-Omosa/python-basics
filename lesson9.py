# LOOPS IN PYTHON
# Loops allow repeated execution of code while a condition is true or for each element in a sequence.

# TYPES OF LOOPS:
# 1. WHILE loop: Repeats as long as the condition is true.
# 2. FOR loop: Iterates over a sequence (like a list, tuple, string, etc.).

# WHILE LOOP
# A while loop executes as long as the specified condition is True.

# Example 1: Infinite loop with a break statement
while True:
    # Prints a message infinitely unless we break out of the loop.
    print("This is a while loop")
    break  # Exits the loop immediately.

# Example 2: Incremental while loop
# Initialize a variable 'a' with the value of 1.
a = 1
while a < 5:  # Condition: loop as long as 'a' is less than 5.
    print(a)  # Print the current value of 'a'.
    a += 1  # Increment 'a' to ensure the condition eventually becomes False.

# Example 3: Using a break statement
b = 2
while b < 6:  # Condition: loop while 'b' is less than 6.
    print(b)  # Print the current value of 'b'.
    if b == 4:  # If 'b' equals 4, exit the loop.
        break
    b += 1  # Increment 'b' after each iteration.

# Example 4: Using a continue statement
c = 3
while c < 7:  # Loop while 'c' is less than 7.
    c += 1  # Increment 'c' at the start of the loop.
    if c == 5:  # Skip the rest of the iteration if 'c' equals 5.
        continue
    print(c)  # Print the value of 'c', excluding 5.

# Example 5: Using else with while loop
d = 4
while d < 8:  # Condition: loop while 'd' is less than 8.
    print(d)  # Print the current value of 'd'.
    d += 1  # Increment 'd'.
else:
    # This block executes once the loop condition becomes False.
    print("d is no longer less than 8")

# FOR LOOP
# A for loop is used to iterate over items in a sequence (list, tuple, string, etc.).

# Example 1: Iterating over a list
brands = ["louis vuitton", "versace", "gucci", "chanel", "balenciaga"]
for x in brands:  # Loops through each item in the list.
    print(x)  # Prints each brand name.

# Example 2: Iterating over a string
# Strings are sequences of characters and can be looped through.
for x in "balenciaga":  # Loops through each character in the string "balenciaga".
    print(x)  # Prints each character individually.

# Example 3: Using a break statement in a for loop
for x in brands:
    print(x)  # Prints the brand name.
    if x == "chanel":  # Exit the loop when "chanel" is found.
        break

# Example 4: Break before printing
for x in brands:
    if x == "gucci":  # If the brand is "gucci", exit the loop.
        break
    print(x)  # Only prints brands before "gucci".

# Example 5: Using a continue statement in a for loop
for x in brands:
    if x == "versace":  # If the brand is "versace", skip this iteration.
        continue
    print(x)  # Prints all brands except "versace".

# RANGE FUNCTION IN LOOPS
# The range() function generates a sequence of numbers, which can be used in loops.

# Example 1: Basic range usage
for x in range(6):  # Generates numbers from 0 to 5 (excludes 6).
    print(x)

# Example 2: Specifying start and end
for x in range(2, 6):  # Generates numbers from 2 to 5.
    print(x)

# Example 3: Specifying an increment
for x in range(2, 30, 3):  # Generates numbers starting at 2, up to 30 (exclusive), incrementing by 3.
    print(x)

# ELSE IN FOR LOOP
# The else block in a for loop runs after the loop completes all iterations unless the loop is terminated by a break.

# Example 1: For loop with else
for x in range(6):  # Loops through numbers 0 to 5.
    print(x)
else:
    print("Finally finished!")  # This message is printed after the loop finishes.

# Example 2: Break prevents the else block
for x in range(6):  # Loops through numbers 0 to 5.
    if x == 3:  # Exit the loop when 'x' equals 3.
        break
    print(x)
else:
    print("Finally finished!")  # This will not execute because the loop was broken.

# NESTED LOOPS
# A nested loop is a loop inside another loop.

# Example: Combine adjectives with fruits
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:  # Outer loop for each adjective.
    for y in fruits:  # Inner loop for each fruit.
        print(x, y)  # Prints every combination of adjectives and fruits.

# PASS STATEMENT
# The pass statement is a placeholder and does nothing. It is used when a loop or block of code cannot be empty.

for x in [0, 1, 2]:  # Loop iterating over a list.
    pass  # Does nothing but prevents a syntax error.

# FILTERING DATA WITH LOOPS
# Example: Filtering and processing a list based on conditions
marks = [91, 82, 73, 64, 55, 46, 37, 28, 19, 90, 98, 87, 76, 65, 54, 43, 32, 21, 12, 23, 34, 45, 56, 67, 78, 89]
for mark in marks:  # Iterate over the list of marks.
    # Check if the mark is between 50 and 100 and is an even number.
    if 50 <= mark <= 100 and mark % 2 == 0:
        print(mark)  # Print the mark if it meets the condition.
