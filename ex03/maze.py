import tkinter as tk
from tkinter import messagebox
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0: 
        cx, cy = mx*100+50, my*100+50
    elif maze_lst[my][mx] == 2:
        cv.coords("tori", cx, cy)
        messagebox.showinfo("clear","clear") 
        root.destroy()
    else: 
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1    
    cv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかどん")
    cv = tk.Canvas(root, width=1500, height=900, bg="black")
    cv.pack()

    maze_lst = mm.make_maze(15, 9)    
    mm.show_maze(cv, maze_lst)

    label = tk.Label(root,  text="Start", font=("ricty Diminished", 20))
    label.place(x=110, y=130)

    tori = tk.PhotoImage(file="ex03/fig/2.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    cv.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    maze_lst[7][13] = 2

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()

