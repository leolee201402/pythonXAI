---

## 📖 一、基本程式語法

### 1. `with open(...) as f:` 讀取檔案

就像打開一本書來讀內容。

```python
with open("檔案路徑", "r", encoding="utf-8") as f:
    print(f.read())
```

👉 `f.read()` 是把整本書的內容讀出來印出來。

---

## 🧮 二、算數運算與順序

### 1. 算數指定運算子（加減乘除等）

```python
a = 1
a += 1  # a = a + 1
a -= 1  # a = a - 1
a *= 2  # a = a * 2
a /= 2  # a = a / 2
a //= 2  # a = a // 2（整除）
a %= 2  # a = a % 2（餘數）
a **= 2  # a = a ** 2（次方）
```

### 2. 運算順序（很重要！）

算式會依照下面的順序來進行：

```
1. 括號 ()
2. 次方 **
3. 乘除取商取餘數 * / // %
4. 加減 + -
5. 比大小 == != > < >= <=
6. not
7. and
8. or
9. 指定運算 = += -= ...
```

---

## 🔁 三、重複做事情（迴圈）

### 1. `while` 迴圈

只要條件是對的，就會一直做下去。

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### 2. `break` 中止迴圈

遇到 `break` 就會立刻跳出來。

```python
while True:
    if 猜對了:
        break
```

---

## 🎲 四、隨機抽籤（random）

```python
import random

random.randrange(7)        # 0~6
random.randrange(1, 6)     # 1~5
random.randrange(1, 6, 2)  # 1, 3, 5

random.randint(1, 6)       # 1~6（包含6）
```

---

## 🎮 五、猜數字遊戲範例

```python
a = random.randint(1, 100)
while True:
    num = int(input("請輸入1~100的數字："))
    if num == a:
        print("猜對了！")
        break
    elif num > a:
        print("太大了")
    else:
        print("太小了")
```

---

## 📦 六、Streamlit 互動網頁程式

### 1. 匯入 Streamlit

```python
import streamlit as st
```

---

## 🧱 七、畫面排版：欄位 `st.columns()`

### 兩欄（1：1）

```python
col1, col2 = st.columns(2)
```

### 三欄（1：2：3）

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

### 用 `with` 把東西放到欄位裡

```python
with col1:
    st.button("按鈕1")
```

---

## 🎛 八、按鈕與文字輸入元件

### 按鈕

```python
st.button("按鈕名稱")
```

### 輸入文字

```python
text = st.text_input("請輸入文字", value="預設文字")
st.write(f"你輸入的是: {text}")
```

---

## 🧠 九、記住變數：`st.session_state`

### 按下按鈕，數字會 +1

```python
if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("按下去加1"):
    st.session_state.ans += 1

st.write(f"ans={st.session_state.ans}")
```

---

## 🔁 十、強制重新整理畫面

```python
st.rerun()
```

---

## 🍔 十一、點餐機功能

### ✅ 初始化點餐清單

```python
if "order" not in st.session_state:
    st.session_state.order = []
```

### ➕ 加餐點

```python
food = st.text_input("請輸入餐點")
if st.button("加入餐點") and food:
    st.session_state.order.append(food)
```

### 📋 顯示點餐清單 + 刪除按鈕

```python
for i, item in enumerate(st.session_state.order):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f"{i+1}. {item}")
    with col2:
        if st.button("刪除", key=f"delete_{i}"):
            st.session_state.order.pop(i)
            st.rerun()
```

### 🔁 重製清單

```python
if st.button("重製清單"):
    st.session_state.order = []
```
