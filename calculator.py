import tkinter as tk
from tkinter import font as tkfont

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x450")
        self.root.resizable(False, False)
        
        # Custom font
        self.default_font = tkfont.Font(family="Arial", size=12)
        self.large_font = tkfont.Font(family="Arial", size=18, weight="bold")
        
        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.display = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=self.large_font, 
            bd=10, 
            insertwidth=2, 
            width=14, 
            borderwidth=4, 
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            button = tk.Button(
                root, 
                text=text, 
                font=self.default_font,
                padx=20, 
                pady=20,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, sticky="nsew")
            
            # Configure row/column weights
            root.rowconfigure(row, weight=1)
            root.columnconfigure(col, weight=1)
        
        # Make buttons expand with window
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        current = self.display_var.get()
        
        if char == 'C':
            self.display_var.set("0")
        elif char == '=':
            try:
                result = str(eval(current))
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
        else:
            if current == "0" or current == "Error":
                self.display_var.set(char)
            else:
                self.display_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    
    # Set window icon (optional)
    try:
        root.iconbitmap('calculator.ico')  # You can provide an icon file if desired
    except:
        pass
    
    root.mainloop()
