import streamlit as st
import openai  # pip install openai

# from utils import load_openai_api

openai.api_key = st.secrets["OPENAI_API_KEY"]  # 設定 OpenAI API 金鑰

if "history" not in st.session_state:  # 初始化歷史紀錄
    st.session_state.history = []  # 如果對話歷史不存在，就初始化為空列表

if "system_message" not in st.session_state:  # 初始化系統訊息
    st.session_state.system_message = (
        "請用繁體字進行後續對話"  #  如果系統訊息不存在，就設定一個預設值
    )

if "model" not in st.session_state:  # 初始化ai模型
    st.session_state.model = "gpt-4o-mini"  # 設定預設模型

#  設置三個列布局，分別佔用 4:2:1 的寬度
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    # 在第一列顯示並更新系統訊息
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )

with col2:
    # 在第二列顯示並選擇ai模型
    st.session_state.model = st.selectbox(
        "AI 模型",
        [
            "gpt-4o-mini",
            "gpt-4o",
            "gpt-4o-search-preview",
        ],
    )


with col3:
    if st.button("🗑️"):  # 在第三列顯示清除按鈕
        st.session_state.history = []  # 按下按鈕後清除歷史紀錄
        st.rerun()  # 重新整理頁面以反映變更

# 從對話紀錄中迭代每一個訊息並顯示
for message in st.session_state.history:
    if message["role"] == "user":  # 如果訊息角色是使用者
        st.chat_message("user", avatar="🪄").write(
            message["content"]
        )  # 顯示使用者訊息，使用指定的頭像
    else:
        st.chat_message("assistant", avatar="✨").write(
            message["content"]
        )  # 顯示ai訊息，使用指定的頭像

prompt = st.chat_input("請輸入想要對話的訊息")  # 顯示對話輸入框，等待使用者輸入訊息
if prompt:  # 如果使用者輸入了訊息
    st.session_state.history.append(
        {"role": "user", "content": prompt}
    )  # 將使用者的訊息加入對話紀錄

    response = openai.chat.completions.create(
        model=st.session_state.model,  # 使用選定的AI模型
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )

    assistant_message = response.choices[0].message.content  # 取得AI助手回傳的訊息內容
    st.session_state.history.append(
        {"role": "assistant", "content": assistant_message}
    )  # 將AI助手的訊息加入對話紀錄
    st.rerun()  # 重新整理頁面以顯示新的訊息
