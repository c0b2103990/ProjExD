import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x600")

entry = tk.Entry(root, width=10, font=("Times New Roman", 40), justify="right")
entry.grid(columnspan = 3)


r = 1
c = 0

def button_click(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)

def button_zero(event):
    entry.insert(tk.END, 0)
    entry.insert(tk.END, 0)

def button_eq(event):
    eqn = entry.get()
    try:
        eval(eqn)
    except SyntaxError:
        entry.delete(0, tk.END)
    else:
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

def button_ac(event):
    entry.delete(0, tk.END)

def button_cr(event):
    rist = entry.get()
    clr = rist[:-1]
    entry.delete(0,tk.END)
    entry.insert(tk.END, clr)

def button_dot(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, ".")


ac = tk.Button(root, text="AC",
               font = ("Times New Roman", 30),
               width=4, height=1)
ac.bind("<1>", button_ac)
ac.grid(row = r, column = c)

cr = tk.Button(root, text="C",
              font = ("Times New Roman", 30),
              width=4, height=1)
cr.bind("<1>", button_cr)
cr.grid(row = r, column = c + 1)

dot = tk.Button(root, text=".",
               font = ("Times New Roman", 30),
               width=4, height=1)
dot.bind("<1>", button_dot)
dot.grid(row = r, column = c + 2)


numbers = list(range(9, -1, -1))
operators = ["00","+", "-", "*", "/"]

for i,num in enumerate(numbers + operators, 1):
    button = tk.Button(root, text=f"{num}",
                      font = ("Times New Roman", 30),
                      width=4, height=1)
    button.bind("<1>", button_click)
    button.grid(row=r + 1, column=c)

    c += 1
    if i%3 == 0:
        r+=1
        c=0
        

eq = tk.Button(root, text="=",
               font = ("Times New Roman", 30),
               width=4, height=1)
eq.bind("<1>", button_eq)
eq.grid(row = r + 1, column = c)


root.mainloop()