以下是你今天上課學到的 Python 指令內容，整理成一篇**適合高中生理解**的清楚筆記 📘
這份筆記包含「檔案讀寫」、「資料夾操作」、「while/for 迴圈」、「隨機數」、「Streamlit 應用程式寫法」等主題。

---

# 🧠 Python 筆記整理（高中生版本・進階篇）

---

## 📁 一、檔案操作（讀取、寫入）

### 🔹 開啟並讀取檔案（read）

```python
f = open("pages/class1-1.py", "r", encoding="utf-8")  # "r" 是讀取
content = f.read()
print(content)
f.close()  # 關閉檔案（很重要！）
```

### ✅ 推薦做法：用 `with` 自動關閉檔案

```python
with open("pages/class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

📌 `with` 可以自動幫你關檔案，就不用寫 `f.close()`

---

### 🔹 檔案模式比較

| 模式  | 說明                                       |
| ----- | ------------------------------------------ |
| `"r"` | 讀檔，檔案不存在會錯誤                     |
| `"w"` | 寫檔（會覆蓋原內容），檔案不存在會自動建立 |
| `"a"` | 續寫檔案，檔案不存在會自動建立             |

---

### 🔹 判斷檔名副檔名

```python
filename = "class1.md"
print(filename.endswith(".md"))  # 結果是 True
```

📌 `.endswith()` 可以檢查檔案是不是特定格式（例如 `.py`, `.txt`）

---

## 📂 二、資料夾與檔案列表

```python
import os

folder_Path = "markdown"
files = os.listdir(folder_Path)
print(files)  # 列出資料夾裡的檔案清單
```

---

## 🔄 三、while 迴圈與 break 指令

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

### 🔹 break：中途跳出迴圈

```python
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
```

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## 🎲 四、隨機數（random）

```python
import random

n = random.randrange(1, 4)  # 產生 1～3 的整數（不含4）
```

### 🔹 統計範例（擲 30 次骰子）

```python
count1 = count2 = count3 = 0
for i in range(30):
    n = random.randrange(1, 4)
    if n == 1:
        count1 += 1
    elif n == 2:
        count2 += 1
    else:
        count3 += 1
    print(n)

print(f"1的次數: {count1}, 2的次數: {count2}, 3的次數: {count3}")
```

### 🔹 其他範例

```python
print(random.randrange(0, 10, 2))  # 產生 0~8 的偶數
print(random.randrange(10, 20))   # 產生 10~19 的整數
```

---

## 🖥️ 五、使用 Streamlit 製作互動網頁

> 📌 Streamlit 是用來做互動式網頁的小工具，非常適合初學者做介面！

### 🔸 標題 + 按鈕排版（使用欄位）

```python
import streamlit as st

st.title("欄位元件")  # 頁面標題
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

---

### 🔸 多欄位排版範例

```python
col3, col4, col5 = st.columns([1, 2, 3])
with col3:
    st.write("欄位3")
    st.write("按鈕3")
with col4:
    st.write("欄位4")
    st.write("按鈕4")
with col5:
    st.write("欄位5")
    st.write("按鈕5")
```

---

### 🔸 文字輸入元件

```python
st.title("文字輸入元件")
text = st.text_input("輸入文字")
st.write("你輸入的文字是:", text)
```

---

## 🧠 六、記住資料：使用 Session State

### 🔸 變數 `ans` 的例子（不會記住每次變化）

```python
ans = 1
st.write(f"ans={ans}")
if st.button("加1"):
    ans += 1
st.write(f"ans={ans}")
```

### 🔸 正確做法：使用 `st.session_state`

```python
if "var1" not in st.session_state:
    st.session_state.var1 = 1

st.write(f"var1={st.session_state.var1}")
if st.button("add 1 to var1"):
    st.session_state.var1 += 1
    st.rerun()  # 重新執行頁面
```

---

## 🍔 七、點餐機小專案（練習 session）

```python
st.title("點餐機")
col1, col2 = st.columns(2)
food = col1.text_input("請輸入餐點")

# 建立購物籃（第一次進來才建立）
if "order" not in st.session_state:
    st.session_state.order = []

# 點「加入」時把餐點加進去
if col2.button("加入", key="add"):
    st.session_state.order.append(food)
    st.rerun()

# 顯示購物籃內容，並提供刪除按鈕
st.write("購物籃:")
for i in range(len(st.session_state.order)):
    col3, col4 = st.columns(2)
    col3.write(st.session_state.order[i])
    if col4.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
```

---

## 🧾 總結重點表

| 主題                 | 重點                  |
| -------------------- | --------------------- |
| 檔案模式             | `r`讀、`w`寫、`a`續寫 |
| `with open(...)`     | 自動關檔案            |
| `.endswith()`        | 判斷檔名結尾          |
| `os.listdir()`       | 列出資料夾內容        |
| `while`, `for`       | 控制流程              |
| `break`              | 強制跳出迴圈          |
| `random.randrange()` | 產生隨機數            |
| `st.button()` 等     | Streamlit 元件        |
| `st.session_state`   | 儲存與記住變數值      |

---

如果你還需要這份整理做成 PDF、小抄、或自動產生測驗題，也可以告訴我，我可以幫你快速生成！👍
