from dotenv import load_dotenv
from enum import IntEnum
import os
from classic_calculator import classic_calculator, classic_calculator_history
from geometrical_calculator import geometrical_calculator, geometrical_calculator_history, calculation_history, save_to_csv


def main_menu():
    print("Choose calculator:")
    print("1. Classic calculator")
    print("2. Geometrical calculator")
    print("3. Show operations history")
    print("4. Save history of operations to csv. file")
    print("5. Exit")
    choice = input("Number of the type of calculator you want to use: ")

    if choice == "1":
        classic_calculator()
    elif choice == "2":
        geometrical_calculator()
    elif choice == "3":
        calculation_history()
    elif choice == "4":
        save_to_csv(classic_calculator_history, geometrical_calculator_history)
    else:
        print("There isn't such an operation, choose other one.")

if __name__ == "__main__":
    main_menu()
