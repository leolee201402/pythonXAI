import streamlit as st  # 匯入 streamlit 模組並重命名為 st

# st.number_input()可以讓使用者輸入數字，設定STEP=1可以讓使用者只能輸入整數
# min_value=0設定最小值為0，max_value=100設定最大值為100
a = st.number_input("請輸入一個整數", step=1, min_value=0, max_value=100)
# st.markdown()可以讓我們在網頁上顯示Markdown格式的文字
st.markdown(f"你輸入的數字是：{a}")


st.markdown("---")
number = st.number_input("請輸入一個分數", step=1, min_value=0, max_value=100)
st.title("練習")

if number >= 90:
    st.markdown("you got A")
elif number >= 80:
    st.markdown("you got B")
elif number >= 70:
    st.markdown("you got C")
elif number >= 60:
    st.markdown("you got D")
else:
    st.markdown("you got f")


st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以在網頁上顯示一個按鈕，使用者可以點擊
# key是按鈕的識別名稱，可以用來區分不同的按鈕
# 如果使用者點擊按鈕，st.button()會回傳True，否則回傳False
st.button("點我", key="button1")

if st.button("點我", key="balloons"):
    st.balloons()  # 顯示氣球動畫
if st.button("點我", key="snow"):
    st.snow()  # 顯示雪花動畫
st.markdown("---")
