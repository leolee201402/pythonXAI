---
## 🧠 Python 指令總整理（國小版）
---

### 🟡 一、Streamlit 網頁互動功能

#### ✅ 1. 匯入工具

```python
import streamlit as st
```

👉 就像打開一個工具箱，叫做 Streamlit，讓我們可以做出互動的網頁。

---

#### ✅ 2. 輸入數字（用滑桿）

```python
a = st.number_input("請輸入一個整數", step=1, min_value=0, max_value=100)
```

👉 顯示一個數字輸入格，讓使用者輸入 0 ～ 100 之間的整數。

---

#### ✅ 3. 顯示內容

```python
st.markdown(f"你輸入的數字是：{a}")
```

👉 把剛剛輸入的數字顯示在畫面上。

---

#### ✅ 4. 判斷分數成績（A\~F）

```python
if number >= 90:
    st.markdown("you got A")
elif number >= 80:
    st.markdown("you got B")
...
```

👉 依照你輸入的分數，告訴你是哪個等級（A\~F）。

---

#### ✅ 5. 按鈕 & 動畫

```python
if st.button("點我", key="balloons"):
    st.balloons()
```

👉 按下按鈕，畫面會出現 🎈 氣球 或 ❄️ 雪花動畫。

---

#### ✅ 6. 數字金字塔

```python
for i in range(1, number + 1):
    st.write(str(i) * i)
```

👉 會印出像這樣的圖案（如果輸入 4）：

```
1
22
333
4444
```

---

### 🔵 二、Python 基本語法

#### ✅ 1. for 迴圈

```python
for i in range(5):
    print(i)
```

👉 重複做事情，這個會印出 0\~4。

---

#### ✅ 2. range 用法

```python
range(1, 5)        # 印出 1, 2, 3, 4
range(1, 10, 2)    # 印出 1, 3, 5, 7, 9
```

---

#### ✅ 3. 計算

```python
a = i * 2
```

👉 可以用變數做數學計算。

---

### 🔶 三、List（像裝東西的盒子）

#### ✅ 1. 建立一個 list

```python
a = [90, 50, 20, 80, 70]
```

👉 像一個裝了五個分數的盒子。

---

#### ✅ 2. 讀取 list 裡的資料

```python
print(a[0])  # 印出第一個
print(a[4])  # 印出第五個
```

👉 編號從 0 開始喔！

---

#### ✅ 3. 切片（取一段資料）

```python
print(name[2:5])  # 從第3個取到第5個（不包含第6個）
print(L[::2])     # 每2個取一個
print(L[1:4:2])   # 從第2到第4，每2個取一個
```

---

#### ✅ 4. list 的長度

```python
len(L)  # 看有幾個東西
```

---

#### ✅ 5. 用 for 讀取 list

```python
for i in L:
    print(i)
```

👉 把 list 裡的每一個東西都印出來。

---

#### ✅ 6. 值的複製（Call by value / reference）

```python
a = [1, 2, 3]
b = a
b[0] = 2
print(a)  # a 也被改變了！
```

✅ 解釋：兩個變數共用同一個盒子！

---

#### ✅ 7. 複製 list

```python
b = a.copy()
```

👉 這樣才會是不同的盒子，互不影響！

---

#### ✅ 8. list 加東西

```python
L.append(4)  # 把 4 加到最後
```

---

#### ✅ 9. list 刪除東西

```python
L.remove("a")  # 移除第一個 "a"
L.pop(0)       # 移除第0個
L.pop()        # 移除最後一個
```

---

#### ✅ 10. 成績平均計算

```python
avg = (midterm[1] + final[1]) / 2
print(avg)
```

---

#### ✅ 11. 編號 + 名字顯示

```python
name = ["Amy", "Mandy", "Peter"]
index = 1
for i in name:
    print(f"{index}號是{i}")
    index += 1
```

👉 顯示：

```
1號是Amy
2號是Mandy
3號是Peter
```

---

## 🎉 總結：你今天學到什麼？

| 類別      | 功能                         | 說明                         |
| --------- | ---------------------------- | ---------------------------- |
| Streamlit | `st.number_input()`          | 讓使用者輸入數字             |
| Streamlit | `st.button()`                | 顯示按鈕，點下去可以觸發事情 |
| Streamlit | `st.balloons()`、`st.snow()` | 出現動畫效果                 |
| 條件判斷  | `if`, `elif`, `else`         | 根據不同情況做不同事         |
| 迴圈      | `for i in range()`           | 重複做事情                   |
| list      | 建立/讀取/新增/刪除          | 像是一排可以裝很多東西的箱子 |
| 複製      | `.copy()`                    | 不共用記憶體                 |
| 切片      | `list[start:end:step]`       | 拿出 list 裡的一段資料       |

---
