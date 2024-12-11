# Python script using if statements to evaluate and print a grade based on an entered score.

# Prompt the user to input their score.
entered_value = input("Enter your score: ")

# Uncomment these lines to check the type of the entered value.
# print(type(entered_value))
# print(type(71))  # Example of an integer type.
# print(type(56.78))  # Example of a float type.

# Check if the input is not a numeric value.
if not entered_value.isnumeric():
    print("This is not a valid number")  # Inform the user that the input is invalid.
    exit(0)  # Exit the program since the input is not valid.

# Convert the valid numeric input into an integer.
score = int(entered_value)

# Evaluate the score and print the corresponding grade.
if score >= 85:
    print("A")  # Excellent performance.
elif score >= 78 and score <= 84:
    print("A-")  # Very good performance.
elif score >= 71 and score <= 77:
    print("B+")  # Good performance.
elif score >= 64 and score <= 70:
    print("B")  # Fairly good performance.
elif score >= 57 and score <= 63:
    print("B-")  # Average performance.
elif score >= 50 and score <= 56:
    print("C+")  # Below-average performance.
elif score >= 43 and score <= 49:
    print("C")  # Needs improvement.
elif score >= 36 and score <= 42:
    print("C-")  # Poor performance.
elif score >= 29 and score <= 35:
    print("D+")  # Very poor performance.
elif score >= 22 and score <= 28:
    print("D")  # Barely passing.
elif score >= 15 and score <= 21:
    print("D-")  # Close to failing.
elif score >= 8 and score <= 14:
    print("E")  # Failing grade.
elif score >= 1 and score <= 7:
    print("F")  # Very poor; lowest grade.
