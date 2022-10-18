import tkinter as tk
import maze_maker as mm
from PIL import Image, ImageTk
import tkinter.messagebox as tkm


#練習5
def key_down(event):
    global key
    key = event.keysym
    print(key)


#練習6
def key_up(event):
    global key
    key = " "


#練習7,11,12
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
        cx, cy = (mx*100)+50 , (my*100)+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)
    if mx ==13 and my == 7:
        tkm.showinfo("ゴール","おめでとう！")
    else:
         root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    #練習1
    root.title("迷えるこうかとん") 

    #練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() 

    #練習9
    maze_lst = mm.make_maze(15,9)
    # print(maze_lst) #1:壁/0:床

    #練習10
    mm.show_maze(canv,maze_lst)

    #練習3
    tori = tk.PhotoImage(file="fig/3.png")
    mx , my = 1, 1
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") 

    #追加機能
    maguma_lst=[[0 for i in range(15)] for y in range(9)]
    for i,y in enumerate(maze_lst):
        for j,x in enumerate(y):
            if x == 1 :
                img = Image.open('maguma.png')
                img = img.resize((100, 100))
                maguma_lst[i][j] = ImageTk.PhotoImage(img)
                canv.create_image(j*100+50, i*100+50, image= maguma_lst[i][j], tag="tile"+str(i)+str(j))
    
    #練習4　現在押されているキー
    key =" "

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    root.mainloop()

