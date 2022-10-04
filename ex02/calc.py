import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("計算機")
root.geometry("400x600")


def btn_clc(event):#ボタンが入力された時の関数
    btn = event.widget
    txt = btn["text"]
   # tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
    entry.insert(tk.END,txt)


def btn_kotae(event):#=が押されたときの関数
    kotae = entry.get()
    res = eval(kotae)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)


def clear(event):##オールクリアの関数
    entry.delete(0,tk.END)


entry = tk.Entry(root, width=13, font=(", 40"), justify="right") #入力画面の表示
entry.grid(row=0, column=0, columnspan=5)


r,c = 2,0#数字のボタンの表示
for i in range(9,-1,-1):
    btn = tk.Button(root,text=f"{i}",font=(" ",30),fg="black",bg="lightgray",width=4,height=2)
    btn .bind("<1>",btn_clc)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 1:
        r += 1
        c = 0

#=ボタンの表示
btn = tk.Button(root,text=f"=",font=(" ",30),bg="LightSteelBlue1",width=8,height=2)
btn.bind("<1>",btn_kotae)
btn.grid(row=r,column=c,columnspan=2)

#オールクリアボタンの表示
btn = tk.Button(root,text=f"AC",font=(" ",30),fg="white",bg="red",width=4,height=2)
btn.bind("<1>",clear)
btn.grid(row=1,column=0)

#演算子の表示
enzansi = ["+","-","*","/"]
a,b=2,3
for i in enzansi:
    btn = tk.Button(root,text=f"{i}",font=(" ",30),fg="White",bg="orange",width=4,height=2)
    btn.bind("<1>",btn_clc)
    btn.grid(row=a,column=b)
    a += 1




root.mainloop()