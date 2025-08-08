---

## 🧠 一、字典（dict）是什麼？

就像一本字典，一個「單字」（key）會對應到一個「解釋」（value）。

```python
d = {"a": 1, "b": 2}
```

這裡：

* "a" 是 key，1 是 value
* "b" 是 key，2 是 value

### 🔎 字典的操作

| 功能          | 說明           | 範例                       |
| ----------- | ------------ | ------------------------ |
| 取得所有 key    | `d.keys()`   | 得到 \['a', 'b']           |
| 取得所有 value  | `d.values()` | 得到 \[1, 2]               |
| 取得全部項目      | `d.items()`  | 得到 \[('a', 1), ('b', 2)] |
| 新增或修改       | `d["c"] = 3` | 加入或改掉 value              |
| 刪除          | `d.pop("a")` | 刪掉 key 為 "a" 的項目         |
| 查詢 key 是否存在 | `"a" in d`   | 回傳 True 或 False          |

### 🧩 字典裡還可以放「清單」或「另一個字典」

```python
d = {
    "a": [1, 2, 3],
    "b": {"c": 4, "d": 5}
}
```

---

## 🏫 二、成績紀錄範例

### 每個學生的成績是一個「字典」中的「字典」

```python
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]},
}
```

### 常見的查詢

```python
grade["小明"]["數學"]       # 拿到數學成績 [85, 75, 65]
grade["小明"]["英文"][0]    # 拿到英文第一次成績 95
```

### 算平均成績

```python
for name, subjects in grade.items():
    chinese = subjects["國文"]
    avg = sum(chinese) / len(chinese)
    print(f"{name}的國文平均是{avg}")
```

---

## 🛠️ 三、函數（function）是什麼？

函數就像一台機器，你把東西丟進去，它會幫你做事情。

### ✅ 最簡單的函數

```python
def hello():
    print("Hello")
```

### 🧃 可以傳資料進去（參數）

```python
def hello(name):
    print(f"Hello, {name}!")
```

### 🎁 可以把答案吐出來（回傳值）

```python
def add(a, b):
    return a + b
```

### 🎁 回傳兩個答案

```python
def add_sub(a, b):
    return a + b, a - b
```

### 🧑‍💼 預設參數

```python
def hello(name, msg="Hello"):
    print(f"{msg}, {name}!")
```

### 🧪 限定資料型態（進階）

```python
def add(a: int, b: int = 0) -> int:
    return a + b
```

---

## 🌍 四、區域變數 vs 全域變數

### 📦 區域變數：只能在函數裡用

```python
def f():
    x = 10  # x 是區域變數
```

### 🗺️ 全域變數：整個程式都可以用

```python
x = 10  # x 是全域變數
```

### ❗ 在函數裡修改全域變數，要加 `global`

```python
x = 5

def f():
    global x
    x = 100
```

---

## 💬 五、用 Streamlit 做聊天頁面（進階）

你寫了一個可以跟 AI 對話的小聊天室系統！

```python
import streamlit as st
import openai

# 設定金鑰、模型、聊天紀錄
# 用 st.chat_input() 讓使用者輸入
# 用 st.chat_message() 顯示訊息
```

裡面用到很多你已經會的東西：

- 字典儲存聊天紀錄
- 條件判斷 if
- 用 `for` 顯示每一句話
- 用 `button` 清除紀錄

---

## 🏁 總結重點表格

| 主題          | 說明                                     |
| ------------- | ---------------------------------------- |
| dict 字典     | 用 key 找 value，像「中文 → 英文」字典   |
| 函數 function | 像一台機器，可以傳資料進去、吐資料出來   |
| 區域/全域變數 | 函數裡 vs 函數外能不能用                 |
| dict + list   | 可以合起來存複雜的資料（像成績系統）     |
| Streamlit     | 做出圖形化的網頁應用，很適合寫聊天機器人 |

---
