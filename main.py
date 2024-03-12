from dotenv import load_dotenv
from enum import IntEnum
import os
import classic_calculator_kuba
import geometrical_calculator_kuba

history = []

def get_name():
    load_dotenv()
    name = os.getenv('USER_NAME')
    return name

def main():
    possibilities = ['Classic_calculator', 'Geometrical_calculator', 'Show_operations_history', 'Exit']
    Possibilities_menu = IntEnum('Possibilities_menu', possibilities)

    name = get_name()
    print(f'Welcome in my calculator {name}!')

    while True:
        print("Choose calculator type: \n"
              "1 - classic calculator\n"
              "2 - geometrical calculator\n"
              "3 - show operations history\n"
              "4 - exit")
        
        choice = int(input("Number of the type of calculator you want to use: "))

        if choice == Possibilities_menu.Classic_calculator:
            classic_calculator_kuba.classic_calculator_kuba(history)
        elif choice == Possibilities_menu.Geometrical_calculator:
            geometrical_calculator_kuba.geometrical_calculator(history)
        elif choice == Possibilities_menu.Show_operations_history:
            print("History of operations: ")
            for operation in history:
                print(operation)    
        elif choice == Possibilities_menu.Exit:
            print("Calculator has been closed")
            break
        else:
            print("There isn't such an operation, choose other one.")

if __name__ == "__main__":
    main()
