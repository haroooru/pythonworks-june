#
# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()

class Movie:
    def __init__(self):
        self.moviename = input("Enter Movie Name: ")
        self.year = input("Enter Release Year: ")
        self.language = input("Enter Language: ")
        self.director = input("Enter Director: ")
        self.rating = float(input("Enter Rating: "))

    def display_details(self):
        print("Movie Name:", self.moviename)
        print("Year:", self.year)
        print("Language:", self.language)
        print("Director:", self.director)
        print("Rating:", self.rating)

    def update_rating(self):
        self.rating = float(input("Enter new rating: "))
        print("Updated Rating:", self.rating)


m = Movie()
m.display_details()
m.update_rating()
m.display_details()


# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.
#


class Vehicle:
    def __init__(self):
        self.brand = input("Enter Brand: ")
        self.model = input("Enter Model: ")
        self.color = input("Enter Color: ")
        self.year = input("Enter Year: ")

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Year:", self.year)


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.mileage = input("Enter Mileage: ")

    def display(self):
        super().display()
        print("Mileage:", self.mileage)


class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc = input("Enter CC: ")

    def display(self):
        super().display()
        print("CC:", self.cc)


c = Car()
c.display()
b = Bike()
b.display()

## Create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.

#
# create an abstract class Shape with abstract methods get_area() and get_perimeter()
# create two subclasses
#  -Rectangle
#  -Square
#
#  -Each class should calculate area() and perimeter() differently


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self):
        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))

    def get_area(self):
        area = self.length * self.breadth
        print("Rectangle Area =", area)

    def get_perimeter(self):
        peri = 2 * (self.length + self.breadth)
        print("Rectangle Perimeter =", peri)


class Square(Shape):
    def __init__(self):
        self.side = float(input("Enter side: "))

    def get_area(self):
        area = self.side * self.side
        print("Square Area =", area)

    def get_perimeter(self):
        peri = 4 * self.side
        print("Square Perimeter =", peri)


r = Rectangle()
r.get_area()
r.get_perimeter()

s = Square()
s.get_area()
s.get_perimeter()


# Multiple Exception Types

try:
    # Normal code to execute

except ValueError:
    # Handling code if ValueError occurs

except ZeroDivisionError:
    # Handling code if ZeroDivisionError occurs

except:
    # Handling code if any other Exception occurs

    # Division with Multiple Exceptions + else + finally

    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        r = n1 / n2
        print("Result =", r)

    except ValueError:
        print("Invalid input! Please enter integers only.")

    except ZeroDivisionError:
        print("Division by zero not allowed!")

    except:
        print("Some other error occurred.")

    else:
        print("No exception in normal block")

    finally:
        print("Finished")
