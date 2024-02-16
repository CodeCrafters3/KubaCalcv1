import os
from dotenv import load_dotenv
import tkinter as tk

def adding(x , y):
    return(x + y)

def subtraction(x , y):
    return(x - y)

def multiplication(x , y):
    return(x * y)

def division(x , y):
    return(x / y)

def modulo(x , y):
    return(x % y)

def power(x , y):
    return(x**y)

def get_name():
    load_dotenv()
    name = os.getenv("IMIE")
    return name

def add_digit(digit):
    current_text = entry.get()    
    new_text = current_text + digit
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)
    
def clear():
    entry.delete(0 , tk.END)
    
def add_dot():
    current_text = entry.get()
    if '.' not in current_text:
        entry.insert(tk.END , '.')
    
#def equals():
    


root = tk.Tk()

label = tk.Label(root , text = 'Welcome!')
label.pack()

entry = tk.Entry(root)
entry.pack()

# first row of buttons
row_1 = tk.Button(root)
row_1.pack()

button_1 = tk.Button(row_1 , text = '1' , command=lambda: add_digit('1'))
button_1.pack(side = tk.LEFT)

button_2 = tk.Button(row_1 , text = '2' , command=lambda: add_digit('2'))
button_2.pack(side = tk.LEFT)

button_3 = tk.Button(row_1 , text = '3' , command=lambda: add_digit('3'))
button_3.pack(side = tk.LEFT)

empty_label = tk.Label(row_1, text = '  ')
empty_label.pack(side=tk.LEFT)

button_adding = tk.Button(row_1 , text = '+' , command = adding)
button_adding.pack(side=tk.LEFT)

button_subtraction = tk.Button(row_1 , text = '-' , command = subtraction)
button_subtraction.pack(side=tk.LEFT)


# second row of buttons
row_2 = tk.Button(root)
row_2.pack()

button_4 = tk.Button(row_2 , text = '4' , command=lambda: add_digit('4'))
button_4.pack(side = tk.LEFT)

button_5 = tk.Button(row_2 , text = '5' , command=lambda: add_digit('5'))
button_5.pack(side = tk.LEFT)

button_6 = tk.Button(row_2 , text = '6' , command=lambda: add_digit('6'))
button_6.pack(side = tk.LEFT)

empty_label = tk.Label(row_2, text = '  ')
empty_label.pack(side=tk.LEFT)

button_multiplication = tk.Button(row_2 , text = '*' , command = multiplication)
button_multiplication.pack(side = tk.LEFT)

button_division = tk.Button(row_2 , text = '/' , command = division)
button_division.pack(side = tk.LEFT)

# third row of buttons
row_3 = tk.Button(root)
row_3.pack()

button_7 = tk.Button(row_3 , text = '7' , command=lambda: add_digit('7'))
button_7.pack(side = tk.LEFT)

button_8 = tk.Button(row_3 , text = '8' , command=lambda: add_digit('8'))
button_8.pack(side = tk.LEFT)

button_9 = tk.Button(row_3 , text = '9' , command=lambda: add_digit('9'))
button_9.pack(side = tk.LEFT)

empty_label = tk.Label(row_3, text = '  ')
empty_label.pack(side=tk.LEFT)

button_modulo = tk.Button(row_3 , text = 'mod' , command = modulo)
button_modulo.pack(side = tk.LEFT)

button_power = tk.Button(row_3 , text = 'pow' , command = power)
button_power.pack(side = tk.LEFT)

#fourth row of buttons
row_4 = tk.Button(root)
row_4.pack()

button_0 = tk.Button(row_4 , text = '0', command=lambda: add_digit('0'))
button_0.grid(row=0, column=0)

empty_label = tk.Label(row_4, text = '  ')
empty_label.grid(row=0, column=1, sticky="nsew")

button_ac = tk.Button(row_4 , text = 'AC' , command = clear)
button_ac.grid(row=0, column=5, sticky="nsew")

button_dot = tk.Button(row_4 , text = '.' , command = add_dot)
button_dot.grid(row=0, column=6, sticky="nsew")

'''button_equals = tk.Button(row_4 , text = '=' , command = equals)
button_equals.grid(row=0, column=7, sticky="nsew")
'''

root.mainloop()