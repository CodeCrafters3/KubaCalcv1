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
    
    def calcuclate_area(self):
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
            triangle_obj = Triangle(a , 0 , 0 ,h)
            area = triangle_obj.calculate_area()
            history.append((f"Triangle area with base {a} and height {h}", area))
            print("The AREA of the triangle is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the length of the first side of the triangle :"))
            b = float(input("Enter the length of the second side of the triangle :"))
            c = float(input("Enter the length of the third side of the triangle :"))
            triangle_obj = Triangle(a , b , c , 0)
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

def rectangle():
    while True:
        print("To calculate THE AREA of rectangle (a * b)  - press '1'")
        print("To calculate THE CIRCUMFERENCE of rectangle ((2 * a) + (2 * b)) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            a = float(input("Enter the length of the first side of the rectangle: "))
            b = float(input("Enter the length of the second side of the rectangle: "))
            rectangle_obj = Rectangle(a , b)
            area = rectangle_obj.calculate_area()
            history.append((f"Rectangle area with sides {a} and {b}", area))
            print("The AREA of the rectangle is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the length of the first side of the rectangle: "))
            b = float(input("Enter the length of the second side of the rectangle: "))
            rectangle_obj = Rectangle(a , b)
            circumference = rectangle_obj.caluclate_circumference()
            history.append((f"Rectangle circumference with sides {a} and {b}", circumference))
            print("The CIRCUMFERENCE of the rectangle is:", circumference)
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")

def rhombus():
    while True:
        print("To calculate THE AREA of rhombus (a * h)  - press '1'")
        print("To calculate THE CIRCUMFERENCE of rhombus (4 * a) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            a = float(input("Enter the length of the  side of the rhombus: "))
            h = float(input("Enter the height of the rhombus: "))
            rhombus_obj = Rhombus(a , h)
            area = rhombus_obj.calculate_area()
            history.append((f"Rhombus area with base {a} and height {h}", area))
            print("The AREA of the rhombus is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the length of the side of the rhombus: "))
            rhombus_obj = Rhombus(a , 0)
            circumference = rhombus_obj.calculate_circumference()
            history.append((f"Rhombus circumference with base {a}", circumference))
            print("The CIRCUMFERENCE of the rhombus is:", circumference)
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")

def regular_pentagon():
    while True:
        print("To calculate THE AREA of regular pentagon (0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a ** 2)  - press '1'")
        print("To calculate THE CIRCUMFERENCE of regular pentagon (5 * a) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            a = float(input("Enter the length of the side of the regular pentagon: "))
            regular_pentagon_obj = RegularPentagon(a)
            area = regular_pentagon_obj.calculate_area()
            history.append((f"Regular pentagon area with side {a}", area))
            print("The AREA of the regular pentagon is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the length of the  side of the regular pentagon: "))
            regular_pentagon_obj = RegularPentagon(a)
            circumference = regular_pentagon_obj.calculate_circumference()
            history.append((f"Regular pentagon circumference with side {a}", circumference))    
            print("The CIRCUMFERENCE of the regular pentagon is:", circumference)
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")

def regular_hexagon():
    while True:
        print("To calculate THE AREA of regular hexagon ((3 * math.sqrt(3) / 2) * a ** 2)  - press '1'")
        print("To calculate THE CIRCUMFERENCE of regular hexagon (6 * a) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            a = float(input("Enter the length of the side of the regular hexagon: "))
            regular_hexagon_obj = RegularHexagon(a)
            area = regular_hexagon_obj.calculate_area()
            history.append((f"Regular hexagon area with side {a}", area))
            print("The AREA of the regular hexagon is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the length of the  side of the regular hexagon: "))
            regular_hexagon_obj = RegularHexagon(a)
            circumference = regular_hexagon_obj.calculate_circumference()
            history.append((f"Regular hexagon circumference with side {a}", circumference))
            print("The CIRCUMFERENCE of the regular hexagon is:", circumference)
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")
    
def rectangular_prism():
    while True:
        print("To calculate THE AREA of rectangular prism (2 * (a * b) + 2 * (a * c) + 2 * (b * c)) - press '1'")
        print("To calculate THE CIRCUMFERENCE of rectangular prism ((4 * a) + (4 * b) + (4 * c)) - press '2'")
        choose = input("Choose operation...")
        if choose == '1':
            a = float(input("Enter the length of the first side of the rectangular prism :"))
            b = float(input("Enter the length of the second side of the rectangular prism :"))
            c = float(input("Enter the length of the third side of the rectangular prism :"))
            rectangular_prism_obj = RectangularPrism(a , b , c)
            area = rectangular_prism_obj.calcuclate_area()
            history.append((f"Rectangular prism area with sides {a}, {b}, {c}", area))
            print("The AREA of the rectangular prism is:", area)
            break
        elif choose == '2':
            a = float(input("Enter the length of the first side of the rectangular prism :"))
            b = float(input("Enter the length of the second side of the rectangular prism :"))
            c = float(input("Enter the length of the third side of the rectangular prism :"))
            rectangular_prism_obj = RectangularPrism(a , b , c)
            circumference = rectangular_prism_obj.calculate_circumference()
            history.append((f"Rectangular prism circumference with sides {a}, {b}, {c}", circumference))
            print("The CIRCUMFERENCE of the rectangular prism is:", circumference)
            break
        else:
            print("Invalid choice. Please enter '1' for area or '2' for circumference.")
            
            

def choose_shape():
    while True:
        print("Please choose a shape for operation:")
        print("1 - Circle")
        print("2 - Triangle")
        print("3 - Square")
        print("4 - Rectangle")
        print("5 - Rhombus")
        print("6 - Regular pentagon")
        print("7 - Regular hexagon")
        print("8 - Rectangular prism")
        shape = input("Enter the number corresponding to the shape: ")
        if shape in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return shape
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

def show_history():
    print("Operation history:")
    for x in history:
        print(x)
        
def save_to_csv(calculations ,  file_name = 'Geometric calculat history.csv'):    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_directory , file_name)
    with open(full_path , 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for expression , result in calculations:
            csv_writer.writerow([f"{expression}={result}"])

        
def main():
    
    while True:
    
        user_choice = choose_shape() 
    
        if user_choice == '1':
            circle()  
        elif user_choice == '2':
            triangle()
        elif user_choice == '3':
            square()    
        elif user_choice == '4':
            rectangle()    
        elif user_choice == '5':
            rhombus()    
        elif user_choice == '6':
            regular_pentagon()    
        elif user_choice == '7':
            regular_hexagon()    
        elif user_choice == '8':
            rectangular_prism()
        else:
            print("Invalid choice. Choose a number between 1 and 8.")
            continue
            
        choice = input("What next?\n"
                       "To continue calculations - press 'continue'\n"
                       "To show history of calculations - press 'history'\n"
                       "To save history of calculations to csv. - press 'csv'\n"
                       "To quit - press 'quit'")
            
        if choice.lower() == 'continue':
            continue
        elif choice.lower() == 'history':
            show_history()
            save_option = input("Do you want to save the history of calculations to a csv. file? (y/n): ")
            if save_option.lower() == 'y':
                save_to_csv(history)
            else:
                continue
        elif choice.lower() == 'csv':
            save_to_csv(history)
        elif choice.lower() == 'quit':
            break
        else:
             print("Invalid choice. Please enter 'display', 'history', 'csv' or 'quit'.")
        
    
    
if __name__ == "__main__":
    main()
    save_to_csv