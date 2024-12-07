# mathematical functionalities
import math

x = 399
square_root = math.sqrt(x)

print("The Square Root of", x, "is", square_root)

rounded_square_root = round(square_root, 2)

print("The Square Root of ", x, "is:", square_root, " which can be rounded off to:", rounded_square_root)

# functions -- arguments
print(rounded_square_root)

# call a function
y = round(8.34345678, 3)
print(y)
print(round(y))

# multiply a number to a power
print(math.pow(2, 4))

# calculate the length in a name
name = "Gilbert Otwoma Omosa"
print(len(name))

# convert name to lower case
name = "GILBERT OTWOMA OMOSA"
print(name.lower())

# convert name to upper case
name = "gilbert otwoma omosa"
print(name.upper())

# convert name to the suitable case
name = "gIlBeRt OtWoMa OmOsA"
print(name.title())

# capitalize the first letter
name = "Gilbert OTWOMA OMOSA"
print(name.capitalize())

# replacing words in a sentence
post = "His speech is very elegant and fluent"
print(post)
new_post = post.replace("elegant", "eloquent")
print(new_post)