以下是整理後的 **Python 筆記（高中生版）**，內容涵蓋了 **OpenAI API、Streamlit 聊天介面、圖片分析、海龜湯遊戲** 等課程重點。

---

# 🧠 Python 筆記整理（OpenAI & Streamlit 實戰篇）

---

## **一、OpenAI API 基礎**

### **1. 設定 API Key**

要使用 OpenAI 的 API，需要先設定金鑰（API Key）：

```python
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 讀取 .env 檔
openai.api_key = os.getenv("OPENAI_API_KEY")  # 取得 API Key
```

---

### **2. 簡單聊天機器人**

使用 `while True` 建立一個可以一直對話的 AI：

```python
while True:
    user_input = input("你: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "請用繁體中文進行後續對話"},
            {"role": "user", "content": user_input},
        ],
    )

    assistant_message = response.choices[0].message.content
    print(f"AI: {assistant_message}")
```

---

### **3. 記住聊天記錄**

我們可以用 `message.append()` 讓 AI 記住之前的對話：

```python
message = [{"role": "system", "content": "請用繁體中文進行後續對話"}]

while True:
    user_input = input("你: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    message.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=message,
    )

    assistant_message = response.choices[0].message.content
    message.append({"role": "assistant", "content": assistant_message})
    print(f"AI: {assistant_message}")
```

---

## **二、Streamlit 聊天功能**

Streamlit 可以快速製作 **聊天介面**。

### **1. 顯示聊天泡泡**

```python
import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的回應")
```

### **2. 使用 `st.session_state` 保存聊天記錄**

```python
if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    st.chat_message("user", avatar="😺").write(message["content"])

prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()
```

---

## **三、AI 聊天室進階版**

我們可以讓使用者選擇 **模型**，清空對話，並且設定系統訊息：

```python
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.session_state.system_message = st.text_input("系統訊息", "請用繁體中文進行後續對話")
with col2:
    st.session_state.model = st.selectbox("AI模型", ["gpt-4o-mini", "gpt-4o"])
with col3:
    if st.button("🗑️"):
        st.session_state.messages = []
        st.rerun()
```

---

## **四、圖片上傳與 AI 分析**

我們可以上傳圖片，將它轉為 **Base64**，再送給 OpenAI 模型分析：

```python
import base64

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="以上傳的圖片", width=300)

    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with open("temp_image.jpg", "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    prompt = st.chat_input("請輸入想要分析的訊息")
    if prompt:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }],
        )
        assistant_message = response.choices[0].message.content
        st.write(assistant_message)
```

---

## **五、海龜湯遊戲**

利用 AI 來模擬「海龜湯」猜題遊戲：

1. 從 JSON 檔讀取題目與答案
2. AI 只能回答 **「是 / 否 / 無關」**
3. 玩家猜對後 AI 公布完整答案

```python
import json, random

with open("question/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    if "pick" not in st.session_state:
        st.session_state.pick = random.randrange(len(data))
    quiz = data[st.session_state.pick]

st.session_state.system_message = f"你是一名海龜湯遊戲的主持,你只能回答(是/否/無關) \
如果玩家的描述很接近正解,則輸出遊戲結束並講述完整正解\n題目:{quiz['title']}\n正解:{quiz['answer']}"
```

---

## **六、使用到的套件**

```text
openai==1.95.0
python-dotenv==1.1.1
streamlit==1.46.1
```

---

## **重點總結**

| 主題           | 重點內容                               |
| -------------- | -------------------------------------- |
| OpenAI API     | `openai.chat.completions.create()`     |
| 聊天記錄       | `message.append()`                     |
| Streamlit 聊天 | `st.chat_message()`、`st.chat_input()` |
| 圖片分析       | `base64.b64encode()`                   |
| 海龜湯遊戲     | JSON 題庫 + AI 回答判斷                |

---

要不要我 **幫你把今天的三篇 Python 筆記（List + Dict + OpenAI）整合成一份完整的 PDF（含程式碼高亮）**？
