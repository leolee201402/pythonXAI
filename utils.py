import streamlit as st
import base64


def load_openai_api() -> str:
    """
    加載 OpenAI API 金鑰。
    Returns:
        str: OpenAI API 金鑰。
    Raises:
        RuntimeError: 如果未找到 OpenAI API 金鑰。
    """

    openai_api_key = st.secrets["OPENAI_API_KEY"]
    if not openai_api_key:
        st.error("未找到 OpenAI API 金鑰。請設置環境變數 OPENAI_API_KEY。")
        st.stop()
    return openai_api_key


def encode_image(image_path):
    """
    將圖片編碼為 base64 字串。\n
    參數：
    - image_path (str)：圖片的檔案路徑。\n
    返回值：
    - str：編碼後的 base64 字串。
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
