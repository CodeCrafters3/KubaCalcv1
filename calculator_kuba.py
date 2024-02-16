import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()  
name = os.getenv('IMIE')

root = tk.Tk()
root.title(f'Welcome in calculator by {name}')

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

entry = tk.Entry(root)
entry.pack(side = tk.TOP , expand = True , fill = tk.BOTH)

def results():
    try:
        result = eval(entry.get())
        entry.delete(0 , tk.END)
        entry.insert(tk.END , result)
    except Exception as e:
        entry.delete(0 , tk.END)
        entry.insert(tk.END , f'Error: {e}')

button = [
        ('1','2','3'),
        ('4','5','6'),
        ('7','8','9'),
        ('0'),
        ('+','-'),
        ('*','/'),
        ('mod','pow'),
        ('.','ac','=')
]

for row in button:
    button_frame = tk.Frame(root)
    button_frame.pack(side = tk.TOP , expand = True , fill = tk.BOTH)
        
    for button_text in row:
        
        if button_text == ' ':
            tk.Label(button_frame , text = '').pack(side = tk.LEFT , expand = True , fill = tk.BOTH)
        
        elif button_text == '=':
            btn = tk.Button(button_frame , text = button_text , command = results)
            btn.pack(side = tk.LEFT , expand = True , fill = tk.BOTH)
        
        elif button_text == 'ac':
            btn = tk.Button(button_frame, text=button_text, command=clear)
            btn.pack(side = tk.LEFT , expand = True , fill = tk.BOTH)
        
        elif button_text in ('+','-' ,'*','/','mod','pow'):
            btn = tk.Button(button_frame , text = button_text , command = lambda op=button_text: add_digit(op))
            btn.pack(side = tk.LEFT , expand = True , fill = tk.BOTH)
        
        else:
            btn = tk.Button(button_frame , text = button_text , command = lambda num=button_text: add_digit(num))
            btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            
root.mainloop()