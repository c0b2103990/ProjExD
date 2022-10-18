import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    cv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかどん") #練習3-1
    cv = tk.Canvas(root, width=1500, height=900, bg="black")
    cv.pack()

    tori = tk.PhotoImage(file="ex03/fig/8.png")
    cx, cy = 300, 400
    cv.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    maze_lst = mm.make_maze(15, 9)
    
    mm.show_maze(cv, maze_lst)



    root.mainloop()

