import streamlit as st  # 匯入 streamlit 模組並重命名為 st


st.markdown("---")
st.markdown("### 數字金字塔")
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=9)
for i in range(1, number + 1):
    st.write(str(i) * i)


st.markdown("---")
