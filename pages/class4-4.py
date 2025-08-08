# def
# 新增一個函數要用 def 開頭，後面接著函數名稱，再加上小括號，最後加上冒號。
# 小括號裡面可以放入傳入函數的參數也可以不放。
def hello():
    print("Hello, World!")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數 name，當呼叫這個函數時，可以傳入一筆資料給 name。
def hello(name):
    print(f"Hello, {name}!")


hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello(i)  # 這裡的 i 會被當作 name 的值


# 有回傳值的函數
# 這個函數會回傳一個值，當呼叫這個函數時，可以把回傳的值存起來。
# 在指令當中只要執行return，就會回傳值，並結束函數。
def add(a, b):  # 可以允許多個傳入參數
    return a + b


print(add(1, 2))
print(add("Hello, ", "World!"))
sum = add(3, 4)  # 可以將回傳值存到變數中
print(sum)


# 有多個回傳值的函數
# 這個函數會回傳兩個值，當呼叫這個函數時，可以把回傳的值存起來。
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum = {sum}, sub = {sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))


# 預設參數
# 可以在函數的參數中設定預設值，當呼叫這個函數時，如果沒有傳入參數，就會使用預設值。
# 多個參數時，有預設值的參數要放在沒有預設值的參數後面。
def hello(name, message="Hello"):
    print(f"{message}, {name}!")


hello("Alice")
hello("Bob", "Good Morning")


# 限制傳入參數型態
# 可以在函數的參數中設定型態，當呼叫這個函數時，可以提示使用者要傳入的參數型態。
# 變數: 型態=預設值
# -> 型態，代表回傳值的型態
def add(a: int, b: int = 0) -> int:
    return a + b


print(add(1, 2))
print(add("Hello, ", "World!"))


import random

b = []


def hello():
    b.append(random.randint(1, 6))  # 1~6


a = int(input("請輸入擲骰子次數："))
for i in range(a):
    hello()
print(b)
