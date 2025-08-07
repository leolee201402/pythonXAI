import streamlit as st
import os

folderpath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderpath)  # 取得資料夾中的所有檔案
# 這時候資料夾可能包含其他檔案，我們只需要.md檔案
files_names = []  # 新增清單來存放 .md檔案
for f in files:  # 逐一檢查每個檔案，看看是否為 .md 結尾
    if f.endswith(".md"):  # 如果檔案是 .md 結尾
        # if ".md" in f:  # 如果檔案名稱中包含 .md
        files_names.append(f)  # 將符合條件的檔案名稱加入清單
files_names.sort()  # 將檔案名稱清單排序，預設是由小到大排序

for f in files_names:  # ["1.md", "2.md", "3.md"] 逐一讀取每個 .md 檔案
    # 用 with open() 讀取檔案內容並存到file變數中，模式為 "r" ，檔案編碼為utf-8
    #  這樣可以避免忘記關閉檔案
    # open 參數說明：(檔案路徑, 開啟模式, 編碼)
    # markdown\class3.md
    with open(f"{folderpath}/{f}", "r", encoding="utf-8") as file:
        # =開啟檔案後，使用 read() 方法讀取檔案內容
        content = file.read()
    with st.expander(f[:-3]):
        st.markdown(content)
