from dotenv import load_dotenv
from enum import Enum
import os
from classic_calculator import classic_calculator, classic_calculator_history
from geometrical_calculator import geometrical_calculator, geometrical_calculator_history, calculation_history, save_to_csv

class CalculatorChoice(Enum):
    Classic = 1
    Geometrical = 2
    Show_history = 3
    Save_to_csv = 4
    exit = 5
    
def get_calculator_choice():
    while True:
        try:
            choice = int(input("Number of the type of calculator you want to use: "))
            if 1 <= choice <= 5:
                return CalculatorChoice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_menu():
    print("Choose calculator:")
    print("1. Classic calculator")
    print("2. Geometrical calculator")
    print("3. Show operations history")
    print("4. Save history of operations to csv. file")
    print("5. Exit")

    calculator_choice = get_calculator_choice
    
    if calculator_choice == CalculatorChoice.Classic:
        classic_calculator()
    elif calculator_choice == CalculatorChoice.Geometrical:
        geometrical_calculator()
    elif calculator_choice == CalculatorChoice.Show_history:
        calculation_history()
    elif calculator_choice == CalculatorChoice.Save_to_csv:
        save_to_csv()
    else:
        print("Exiting...")

if __name__ == "__main__":
    main_menu()
