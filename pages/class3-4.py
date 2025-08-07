import random

a = random.randint(1, 100)  # 1~100
print("歡迎來到猜數字遊戲！")
while True:  # 無限迴圈
    input_number = int(input("請輸入一個1-100的數字："))  # 讓使用者輸入一個數字
    if input_number == a:
        print("恭喜你猜對了！")
        break
    elif input_number > a:
        print("很遺憾，你猜的數字太大了！")
    elif input_number < a:
        print("很遺憾，你猜的數字太小了！")
45
