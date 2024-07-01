import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def func(button):
    current=text.get()
    if button=='=':
        try:
            equation=text.get()
            return text.set(str(eval(equation)))
        except ZeroDivisionError:
            messagebox.showwarning('Warning','Zero Divison Error')
            return text.set('0')
        except ValueError:
            messagebox.showwarning('Warning','Value Error')
            return text.set('0')
        except SyntaxError:
            messagebox.showwarning('Warning','Wrong Operation')
            return text.set('0')
        except:
            messagebox.showwarning('Warning','Unknow error ocurred')
            return text.set('0')
    
    else:
        if current[-1] not in '+/-*' or button not in '+-/*':
            if len(current)==1 and current=='0':
                return text.set(button)
            else:
                return text.set(current+button)

#Main App
app = tk.Tk()
app.geometry('300x400')
app.minsize(width=300,height=400)
app.title('Calculator')
app.configure(bg='black')


text = tk.StringVar()
text.set('0')

# Display
text_area = tk.Label(app, bg='black', width=50, textvariable=text, font=('Courier New CYR', 30, 'bold'), fg='white')
text_area.pack(padx=20, pady=20)

# Button Frame
buttons_frame = tk.Frame(app, width=300, height=320)
buttons_frame.pack(expand=True, fill="both")

# Grid system for buttons
for i in range(4):
    buttons_frame.grid_rowconfigure(i, weight=1)
    buttons_frame.grid_columnconfigure(i, weight=1)

# Buttons
buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('+', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
    ('.', 3, 0), ('0', 3, 1), ('*', 3, 2), ('=', 3, 3),
]

# Creating Buttons
for (btn_text, row, col) in buttons:
    color = 'orange' if btn_text in '+-/*=' else '#666666'
    button = tk.Button(buttons_frame, text=btn_text, bg=color, command=lambda t=btn_text: func(t),
                       font=('Courier New CYR', 30, 'bold'), fg='white')
    button.grid(row=row, column=col, sticky="nsew")


app.mainloop()