import pstats
import random 
import datetime

def kaito(y):
    st=datetime.datetime.now()
    ans=[]
    yans=int(input("欠損文字はいくつあるでしょか？:"))
    if yans == len(y):
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        for i in range(len(y)):
            yans=input(f"{i+1}文字目を入力してください。")
            ans.append(yans)
        if set(y)==set(ans):
            print("正解です！")
        else:
            print("不正解です。またチャレンジしてね")
        ed=datetime.datetime.now()
        print(f"{ed-st}秒かかったよ")
    else:
        kaito(y)

if __name__ == "__main__":
    x = [chr(random.randint(65,90)) for i in range(10)]
    a = " ".join(x)
    print(a)
    y = [random.choice(x) for i in range(random.randint(1,9))]
    b = " ".join(y)
    print(b)
    for num in y:
        x.remove(num)
    c = " ".join(x)
    print(f"対象文字:{a}\n欠損文字:{b}\n表示文字:{c}")
    kaito(y)
