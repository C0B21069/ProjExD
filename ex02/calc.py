import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("計算機")
root.geometry("300x500")


def btn_clc(event):
    btn = event.widget
    txt = int(btn["text"])
    tkm.showinfo(txt,f"{txt}のボタンがクリックされました")


r,c = 0,0
for i in range(9,-1,-1):
    btn = tk.Button(root,text=f"{i}",font=(" ",30),width=4,height=2)
    btn .bind("<1>",btn_clc)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 1:
        r += 1
        c = 0




root.mainloop()