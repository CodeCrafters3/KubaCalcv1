import os
import csv
import math

history = []

class Circle:    
    
    def __init__(self , r):
        self.r = r
                
    def calculate_area(self):
        return math.pi * self.r ** 2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.r
    
class Triangle:
    
    def __init__(self, a , b , c , h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        
    def calculate_area(self):
        return 1/2 * self.b * self.h
    
    def calculate_circumference(self):
        return self.a + self.b + self.c
      
class Square:
    
    def __init__(self , a):
        self.a = a
        
    def calculate_area(self):
        return self.a ** 2
    
    def calculate_circumference(self):
        return 4 * self.a
        
class Rectangle:
    
    def __init__(self , a , b):
        self.a = a
        self.b = b
    
    def calculate_area(self):
        return self.a * self.b
    
    def caluclate_circumference(self):
        return (2 * self.a) + (2 * self.b)
    
class Rhombus:
    
    def __init__(self , a , h):
        self.a = a
        self.h = h
    
    def calculate_area(self):
        return self.a * self.h
    
    def calculate_circumference(self):
        return 4 * self.a
    
class RegularPentagon:
    
    def __init__(self , a):
        self.a = a
    
    def calculate_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.a ** 2
    
    def calculate_circumference(self):
        return 5 * self.a
    
class RegularHexagon:
    
    def __init__(self , a):
        self.a = a
    
    def calculate_area(self):
        return (3 * math.sqrt(3) / 2) * self.a ** 2
    
    def calculate_circumference(self):
        return 6 * self.a
    
class RectangularPrism:
    
    def __init__(self , a , b , c):
        self.a = a
        self.b = b
        self.c = c
    
    def caluclate_area(self):
        return 2 * (self.a * self.b) + 2 * (self.a * self.c) + 2 * (self.b * self.c)
    
    def calculate_circumference(self):
        return (4 * self.a) + (4 * self.b) + (4 * self.c)
    
    
def circle():
    while True:
        print("To calculate THE AREA of a circle (π * r^2) - press '1'")
        print("To calculate THE CIRCUMFERENCE of a circle (2 * π * r) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            r = float(input("Enter the radius of the circle: "))
            circle_obj = Circle(r)
            area = circle_obj.calculate_area()
            history.append((f"Circle area with radius {r}", area))
            print("The AREA of the circle is:", area)
            break
        elif choose == '2':
            r = float(input("Enter the radius of the circle: "))
            circle_obj = Circle(r)
            circumference = circle_obj.calculate_circumference()
            history.append((f"Circle circumference with radius {r}", circumference))
            print("The CIRCUMFERENCE of the circle is:", circumference)
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")

def triangle():
    while True:
        print("To calculate THE AREA of triangle (1/2 * a * h) - press '1'")
        print("To calculate THE CIRCUMFERENCE of triangle (a + b + c) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            a = float(input("Enter the base of the triangle: "))
            h = float(input("Enter the height of the triangle: "))
            triangle_obj = Triangle(a , h)
            area = triangle_obj.calculate_area()
            history.append((f"Triangle area with base {a} and height {h}", area))
            print("The AREA of the triangle is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the length of the first side of the triangle :"))
            b = float(input("Enter the length of the second side of the triangle :"))
            c = float(input("Enter the length of the third side of the triangle :"))
            triangle_obj = Triangle(a , b , c)
            circumference = triangle_obj.calculate_circumference()
            history.append((f"Triangle circumference with sides {a}, {b}, and {c}", circumference))
            print("The CIRCUMFERENCE of the triangle is:", circumference)
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")
            
def square():
    while True:
        print("To calculate THE AREA of square (a ** 2) - press '1'")
        print("To calculate THE CIRCUMFERENCE of square (4 * a) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            a = float(input("Enter the lengths of the side of the square: "))
            square_obj = Square(a)
            area = square_obj.calculate_area()
            history.append((f"Square area with side {a}", area))
            print("The AREA of the square is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the lengths of the side of the square: "))
            square_obj = Square(a)
            circumference = square_obj.calculate_circumference()
            print("The CIRCUMFERENCE of the square is:", circumference)
            history.append((f"Square circumference with side {a}", circumference))
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")     
        
