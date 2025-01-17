import math  # Importing math module to use math.pi for more accuracy in calculations

class Cylinder:
    def __init__(self, radius, height, color):
        # Initialize cylinder properties: radius, height, and color
        self.radius = radius
        self.height = height
        self.color = color

    def calc_area(self, is_closed=True):
        # Calculate the surface area of the cylinder, depending on whether it is closed or open
        if is_closed:
            # Surface area for closed cylinder: 2πr² + 2πrh
            area = 2 * math.pi * self.radius ** 2 + 2 * math.pi * self.radius * self.height
            print(f"The total surface area of the closed cylinder is: {area:.2f} square units")
        else:
            # Surface area for open cylinder: πr² + 2πrh
            area = math.pi * self.radius ** 2 + 2 * math.pi * self.radius * self.height
            print(f"The total surface area of the open cylinder is: {area:.2f} square units")

    def calc_volume(self):
        # Calculate the volume of the cylinder: πr²h
        volume = math.pi * self.radius ** 2 * self.height
        print(f"The volume of the cylinder is: {volume:.2f} cubic units")

# Creating cylinder objects with different properties
afrigas = Cylinder(radius=15, height=60, color="blue")
rubis = Cylinder(radius=10, height=30, color="green")
shell = Cylinder(radius=20, height=120, color="orange")

# Perform calculations on each cylinder object
afrigas.calc_area(is_closed=False)  # Open cylinder (no closed ends)
rubis.calc_area()  # Closed cylinder (default is closed)
shell.calc_volume()  # Calculate and print volume for the shell cylinder


# Used .2f to format the printed area and volume values to two decimal places