import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x500")
r = 0
c = 0

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo(f"{num}", f"{num}ボタンが押されました")
    

for i,num in enumerate(range(9 ,-1, -1), 1):
    button = tk.Button(root, text=f"{num}",
                      font = ("Times New Roman", 30),
                      width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row=r, column=c)

    c += 1
    if i%3 == 0:
        r+=1
        c=0                    
                    


root.mainloop()