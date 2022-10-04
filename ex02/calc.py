import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("計算機")
root.geometry("300x500")


def btn_clc(event):
    btn = event.widget
    txt = btn["text"]
   # tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
    entry.insert(tk.END,txt)


def btn_kotae(event):
    kotae = entry.get()
    res = eval(kotae)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)


entry = tk.Entry(root, width=10, font=(", 40"), justify="right") 
entry.grid(row=0, column=0, columnspan=3)


r,c = 1,0
for i in range(9,-1,-1):
    btn = tk.Button(root,text=f"{i}",font=(" ",30),width=4,height=2)
    btn .bind("<1>",btn_clc)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 1:
        r += 1
        c = 0


btn = tk.Button(root,text=f"+",font=(" ",30),width=4,height=2)
btn.bind("<1>",btn_clc)
btn.grid(row=r,column=c)


btn = tk.Button(root,text=f"=",font=(" ",30),width=4,height=2)
btn.bind("<1>",btn_kotae)
btn.grid(row=r,column=c+1)


root.mainloop()