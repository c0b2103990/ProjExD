
import random
def shutudai(q_list):
    global q
    q = random.choice(q_list)
    print("問題：" + q["q"])
    return q["q"]

def kaido(a_list):
    a = input("答えは：")
    if a in q["a"]:
        print("正解です。")
    else:
        print("不正解です。")

if __name__ == "__main__":
    q_list = [{"q": "1 + 1 = ?", "a": "2"},
              {"q": "3 + 3 = ?", "a": "6"}, 
              {"q": "5 + 5 = ?", "a": "10"}]
    a_list = shutudai(q_list)
    kaido(a_list)    

    
