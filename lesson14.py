from abc import ABC, abstractmethod

# Abstract Base Class
class Person(ABC):
    """
    Abstract base class to serve as a blueprint for all person-related classes.
    """
    @abstractmethod
    def show_details(self):
        """
        Abstract method that must be implemented by all subclasses.
        """
        pass


# Suspect Class
class Suspect(Person):
    """
    Represents a generic suspect with basic details and behavior.
    Inherits from the abstract Person class.
    """
    def __init__(self, name, age, height, gender, id_number, crime):
        """
        Initializes a suspect object with the given details.
        """
        self.name = name  # Name of the suspect
        self.age = age  # Age of the suspect
        self.height = height  # Height of the suspect in cm
        self.gender = gender  # Gender of the suspect
        self.id_number = id_number  # Unique ID number of the suspect
        self.crime = crime  # Crime committed by the suspect

    def show_details(self):
        """
        Displays the details of the suspect.
        Overrides the abstract method from the Person class.
        """
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height} cm')
        print(f'Gender: {self.gender}')
        print(f'ID: {self.id_number}')
        print(f'Crime: {self.crime}')


# ConvictedCriminal Class
class ConvictedCriminal(Suspect):
    """
    Represents a convicted criminal with additional details about their prison term.
    Inherits from the Suspect class.
    """
    def __init__(self, name, age, height, gender, id_number, crime, prison_term):
        """
        Initializes a convicted criminal object with basic suspect details and prison term.
        """
        super().__init__(name, age, height, gender, id_number, crime)  # Initialize base class attributes
        self.prison_term = prison_term  # Prison term in years

    def show_details(self):
        """
        Displays the details of the convicted criminal, including their prison term.
        Overrides the `show_details` method from the Suspect class.
        """
        super().show_details()  # Call the parent method to display basic details
        print(f'Prison Term: {self.prison_term} years')  # Add prison term information


# Case Class
class Case:
    """
    Represents a legal case that involves multiple suspects.
    Demonstrates composition by including suspect objects.
    """
    def __init__(self, case_number, description):
        """
        Initializes a case object with a unique case number and description.
        """
        self.case_number = case_number  # Unique identifier for the case
        self.description = description  # Brief description of the case
        self.suspects = []  # List to store associated suspects

    def add_suspect(self, suspect):
        """
        Adds a suspect to the case.
        """
        self.suspects.append(suspect)

    def show_case_details(self):
        """
        Displays the case details, including a list of all suspects.
        """
        print(f"Case Number: {self.case_number}")
        print(f"Description: {self.description}")
        print("Suspects:")
        for suspect in self.suspects:  # Loop through all suspects and display their details
            suspect.show_details()
            print("-" * 30)  # Separator for better readability


# Example Usage
# Create a case
case = Case("C1234", "Bank Heist")  # Case with a unique number and description

# Create suspects
sus_1 = Suspect("Clyde Barrow", 28, 181, "Male", "10234408", "Bank Robbery")  # Regular suspect
sus_2 = ConvictedCriminal("Bonnie Parker", 27, 160, "Female", "10234409", "Armed Robbery", 10)  # Convicted criminal

# Add suspects to the case
case.add_suspect(sus_1)
case.add_suspect(sus_2)

# Display case details
case.show_case_details()
