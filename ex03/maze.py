import tkinter as tk

#練習5
def key_down(event):
    global key
    key = event.keysym
    print(key)


#練習6
def key_up(event):
    global key
    key = " "


#練習7
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
    # if key == "o": 右上
    #     cy -= 20
    #     cx += 20
    canv.coords("tori", cx, cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    #練習1
    root.title("迷えるこうかとん") 

    #練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() 

    #練習3
    tori = tk.PhotoImage(file="fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") 

    #練習4　現在押されているキー
    key =" "

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    root.mainloop()

