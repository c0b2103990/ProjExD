from os import remove
import random

alpha_num = 26
taisyou_num = 10
kesonn_num = 2
list_a = []

def shutudai(list_a):
    global taisyou
    taisyou = random.sample(list_a, taisyou_num)
    print("対象文字：")
    for i in sorted(taisyou):
        print(i, end=" ")
    print()


    global kesonn
    kesonn = random.sample(taisyou, kesonn_num)
    print("欠損文字：")
    for j in kesonn:
        print(j, end=" ")
        taisyou.remove(j)
    print()


    print("表示文字：")
    random.shuffle(taisyou)
    for k in taisyou:
        print(k, end = " ")
    print()

def kaido():
    a = int(input("欠損文字はいくつあるでしょうか？："))
    if a == 2:
        print("正解です。それでは、具体的に欠損文字を１つずつ実入力してください")
        a1 = input("1つ目の文字を入力してください：")
        a2 = input("2つ目の文字を入力してください：")
        if a1 in kesonn and a2 in kesonn:
            print("正解です。")
        else:
            print("不正解です。またチャレンジしてください。")
            shutudai(list_a)
            kaido()
    else:
        print("不正解です。またチャレンジしてください。")
        shutudai(list_a)
        kaido()


    



if __name__ == "__main__":
    for i in range(65, 91): #A~Zリスト
        list_a.append(chr(i)) 
    shutudai(list_a)
    kaido()
