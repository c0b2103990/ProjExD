import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかどん") #練習3-1
    cv = tk.Canvas(root, width=1500, height=900, bg="black")
    cv.pack()

    tori = tk.PhotoImage(file="ex03/fig/8.png")
    cx, cy = 300, 400
    cv.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<keyPress>", key_down)
    root.mainloop()

