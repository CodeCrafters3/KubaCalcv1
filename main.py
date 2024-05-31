from dotenv import load_dotenv
from enum import Enum
import os
from classic_calculator import run_classic_calculator, classic_calculator_history, save_to_csv_classic
from geometrical_calculator import run_geometrical_calculator, geometrical_calculator_history, save_to_csv_geometrical

class CalculatorChoice(Enum):
    Classic = 1
    Geometrical = 2
    Show_classic_calculation_history = 3
    Show_geometerical_calculation_history = 4
    Save_to_csv_classic_calculations = 5
    Save_to_csv_geometrical_calculations = 6
    exit = 7

def get_calculator_choice():
    while True:
        try:
            choice = int(input("Number of the type of calculator you want to use: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_menu():
    while True:
        print("Choose calculator:")
        print("1. Classic calculator")
        print("2. Geometrical calculator")
        print("3. Show classic calculator operations history")
        print("4. Show classic geometrical operations history")
        print("5. Save history of classic calculator operations to csv. file")
        print("6. Save history of geometrical calculator operations to csv. file")
        print("7. Exit")

        calculator_choice = get_calculator_choice()

        if calculator_choice == 1:
            run_classic_calculator()
        elif calculator_choice == 2:
            run_geometrical_calculator()
        elif calculator_choice == 3:
            print("Classic Calculator History:")
            for operation in classic_calculator_history:
                print(operation)
        elif calculator_choice == 4:
            print("Geometrical Calculator History:")
            for operation in geometrical_calculator_history:
                print(operation)
        elif calculator_choice == 5:
            save_to_csv_classic(classic_calculator_history)
        elif calculator_choice == 6:
            save_to_csv_geometrical(geometrical_calculator_history)
        elif calculator_choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main_menu()