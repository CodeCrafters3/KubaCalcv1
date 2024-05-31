import os
import csv
from dotenv import load_dotenv
import tkinter as tk

classic_calculator_history = []

load_dotenv()
name = os.getenv('IMIE')

def adding(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def modulo(x, y):
    return x % y

def power(x, y):
    return x ** y

def add_digit(digit, entry):
    current_text = entry.get()
    new_text = current_text + digit
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)

def clear(entry):
    entry.delete(0, tk.END)

def add_dot(entry):
    current_text = entry.get()
    if '.' not in current_text:
        entry.insert(tk.END, '.')

def calculation_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation history:")
    history_text = tk.Text(history_window)
    history_text.pack(expand=True, fill=tk.BOTH)
    for calculation in classic_calculator_history:
        history_text.insert(tk.END, f"{calculation[0]} = {calculation[1]}\n")

def save_to_csv_classic(calculations, file_name='Calculation history.csv'):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_directory, file_name)
    with open(full_path, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for expression, result in calculations:
            csv_writer.writerow([f"{expression}={result}"])

def classic_calculator(entry):
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        classic_calculator_history.append((expression, result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f'Error: {e}')

def run_classic_calculator():
    root = tk.Tk()
    root.title(f'Welcome in calculator by {name}')
    
    entry = tk.Entry(root)
    entry.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    button = [
        ('1', '2', '3'),
        ('4', '5', '6'),
        ('7', '8', '9'),
        ('0',),
        ('+', '-'),
        ('* ', '/'),
        ('modulo', '  power'),
        ('.', 'ac', '='),
        ('history',),
        ('download history to csv.',)
    ]

    for row in button:
        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
        for button_text in row:
            if button_text == '=':
                btn = tk.Button(button_frame, text=button_text, command=lambda e=entry: classic_calculator(e))
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            elif button_text == 'ac':
                btn = tk.Button(button_frame, text=button_text, command=lambda e=entry: clear(e))
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            elif button_text == 'history':
                btn = tk.Button(button_frame, text=button_text, command=calculation_history)
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            elif button_text == 'download history to csv.':
                btn = tk.Button(button_frame, text=button_text, command=lambda: save_to_csv_classic(classic_calculator_history))
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            elif button_text in ('+', '-', '* ', '/'):
                btn = tk.Button(button_frame, text=button_text, command=lambda op=button_text, e=entry: add_digit(op, e))
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            elif button_text == 'modulo':
                btn = tk.Button(button_frame, text=button_text, command=lambda op="%", e=entry: add_digit(op, e))
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            elif button_text == '  power':
                btn = tk.Button(button_frame, text=button_text, command=lambda op="**", e=entry: add_digit(op, e))
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            else:
                btn = tk.Button(button_frame, text=button_text, command=lambda num=button_text, e=entry: add_digit(num, e))
                btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    root.mainloop()