import streamlit as st

# 初始化清單
if "order" not in st.session_state:
    st.session_state.order = []

st.title("🍽️ 我的點餐機")

# 功能 2：輸入餐點
st.subheader("➕ 輸入餐點")
food = st.text_input("請輸入餐點名稱")

if st.button("加入餐點"):
    if food:
        st.session_state.order.append(food)
        st.success(f"✅ 已加入：{food}")
    else:
        st.warning("⚠️ 請輸入餐點名稱")

st.write("---")

# 功能 3：顯示清單，每個餐點有獨立刪除按鈕
st.subheader("📋 目前點餐清單")

delete_index = None  # 儲存要刪除的餐點索引

if st.session_state.order:
    for i, item in enumerate(st.session_state.order):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{i+1}. {item}")
        with col2:
            if st.button("刪除", key=f"delete_{i}"):
                delete_index = i

    # 刪除操作在迴圈外面執行
    if delete_index is not None:
        st.session_state.order.pop(delete_index)
        st.rerun()  # ✅ 使用新版的 rerun()
else:
    st.write("尚未點任何餐點")

st.write("---")

# 功能 1：重製清單
if st.button("🔁 重製點餐清單"):
    st.session_state.order = []
    st.success("✅ 點餐清單已重製")
