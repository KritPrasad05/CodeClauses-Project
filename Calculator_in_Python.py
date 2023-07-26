import tkinter as tk

def on_button_click(symbol):
    entry_text.set(entry_text.get() + symbol)

def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(result)
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        entry_text.set("Error")

def clear():
    entry_text.set("")

# Create the main tkinter window
root = tk.Tk()
root.title("Calculator")

# Entry box for displaying and entering expressions
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=5, insertwidth=4, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define buttons for numbers and symbols
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons and assign functions to them
for symbol, row, col in buttons:
    btn = tk.Button(root, text=symbol, padx=20, pady=20, font=("Arial", 15),
                    command=lambda sym=symbol: on_button_click(sym) if sym != '=' else calculate())
    btn.grid(row=row, column=col)

# Clear button
clear_btn = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 15), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4)

root.mainloop()
