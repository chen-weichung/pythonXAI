import streamlit as st

with st.expander("class1.課堂筆記"):
    st.write(
        """
    當然可以！以下是把你今天學到的 Python 指令，整理成一份適合**國小學生**閱讀的筆記，使用簡單易懂的語言來說明各個部分：

    ---

    # 🐍 Python 初學者筆記（國小版）

    ## 🖨️ 1. print() 是什麼？

    `print()` 是一個指令，可以把你想說的話或東西「顯示」在畫面上！

    ```python
    print("Hello")  # 顯示 Hello
    print("what's your name?")  # 顯示 what's your name?
    ```

    ---

    ## 💬 2. 註解是什麼？

    「註解」是給人看的說明，電腦不會執行。

    * **單行註解**：在句子前面加 `#`

    ```python
    # 這是一行註解
    ```

    * **多行註解**：用 `\\\"""` 包起來

    ```python
    \\\"""
    這是多行註解
    可以寫很多行喔！
    \\\"""
    ```

    * 快速註解：按下 `Ctrl + ?`（視你的鍵盤設定可能不一樣）

    ---

    ## 🔢 3. 常見資料的種類（資料型態）

    | 例子        | 資料型態  | 說明       |
    | --------- | ----- | -------- |
    | `1`       | int   | 整數       |
    | `1.0`     | float | 小數       |
    | `"apple"` | str   | 文字（字串）   |
    | `True`    | bool  | 是/否（布林值） |
    | `False`   | bool  | 是/否（布林值） |

    ```python
    print(1)        # 整數
    print(1.234)    # 小數
    print("apple")  # 文字
    print(True)     # 是
    print(False)    # 否
    ```

    ---

    ## 📦 4. 變數是什麼？

    變數就像一個裝東西的盒子，可以放數字、文字或別的東西。

    ```python
    a = 10       # 把數字10放進 a
    print(a)     # 顯示 a 裡面的東西

    a = "apple"  # 把文字"apple"放進 a
    print(a)     # 再次顯示 a
    ```

    ---

    ## ➕ 5. 運算符號

    | 符號   | 功能      | 範例           |
    | ---- | ------- | ------------ |
    | `+`  | 加法      | `1 + 1`      |
    | `-`  | 減法      | `5 - 2`      |
    | `*`  | 乘法      | `2 * 3`      |
    | `/`  | 除法      | `6 / 2`      |
    | `//` | 整數除法    | `7 // 2` → 3 |
    | `%`  | 餘數（mod） | `7 % 2` → 1  |
    | `**` | 次方      | `2 ** 3` → 8 |

    ### 運算順序

    1. 括號 `()`
    2. 次方 `**`
    3. 乘除 `% // / *`
    4. 加減 `+ -`

    ---

    ## 🧩 6. 字串格式化（f-string）

    可以把變數放進字串裡，用 `{}` 包起來！

    ```python
    name = "apple"
    age = 18
    print(f"Hello, my name is {name}, I am {age} years old.")
    ```

    ---

    ## 📏 7. 看資料的長度和型態

    ```python
    print(len("apple"))  # 看字串長度（有幾個字）
    print(type(1))       # 看資料型態（int）
    print(type("apple")) # 看資料型態（str）
    ```

    ---

    ## 🔄 8. 資料型態轉換（Type Conversion）

    | 原來的型態       | 要轉成                | 範例 |
    | ----------- | ------------------ | -- |
    | float → int | `int(1.2)` → 1     |    |
    | int → float | `float(1)` → 1.0   |    |
    | int → str   | `str(1)` → `"1"`   |    |
    | int → bool  | `bool(1)` → `True` |    |

    ```python
    print(int(1.2))
    print(float("1.234"))
    print(str(123))
    print(bool(0))  # 0是False，其它是True
    ```

    ---

    ## 🎤 9. 輸入 input()

    用 `input()` 可以讓使用者輸入東西。

    ```python
    a = input("請輸入一些數字:")
    print(int(a) + 10)  # 把輸入的數字+10
    print(type(a))      # 輸入的結果會是字串（str）
    ```

    ---

    ## 🌐 10. 使用 Streamlit 做網頁介面

    Streamlit 是一種可以把 Python 程式變成網頁的小工具！

    ### 安裝方式

    ```bash
    pip install -U streamlit
    ```

    ### 基本指令

    ```python
    import streamlit as st

    st.title("這是標題")
    st.write("這是一般的內容")
    st.text("這是純文字")
    ```

    ### 顯示 Markdown 樣式（標題、列表、粗體、程式碼）

    ```python
    st.markdown(\\\"""
    # 這是最大標題
    ## 這是第二大標題
    ### 這是第三大標題
    #### 第四大標題
    - 第一個項目
    - 第二個項目
    - 第三個項目

    **粗體文字**
    *斜體文字*
    `這是程式碼`
    \\\""")
    ```



    """
    )
with st.expander("class2.課堂筆記"):
    st.write(
        """
   # 🐍 Python 初學者筆記（高中版）

---

## 1️⃣ 比較運算子（用來比較兩個東西）

| 運算子 | 說明       | 範例     | 結果  |
| ------ | ---------- | -------- | ----- |
| `==`   | 等於       | `1 == 1` | True  |
| `!=`   | 不等於     | `1 != 1` | False |
| `>`    | 大於       | `1 > 1`  | False |
| `<`    | 小於       | `1 < 1`  | False |
| `>=`   | 大於或等於 | `1 >= 1` | True  |
| `<=`   | 小於或等於 | `1 <= 1` | True  |

---

## 2️⃣ 邏輯運算子（讓條件變更強大）

### `and`（而且）

兩邊都要是 `True`，才會回傳 `True`

```python
print(True and True)  # True
print(True and False)  # False
```

### `or`（或者）

只要有一邊是 `True`，就會回傳 `True`

```python
print(True or False)  # True
print(False or False)  # False
```

### `not`（反過來）

把 `True` 變 `False`，`False` 變 `True`

```python
print(not True)  # False
```

---

## 3️⃣ 運算子優先順序（誰先算？）

1. `()` 括號先算
2. `**` 次方
3. `* / // %` 乘、除、整數除、餘數
4. `+ -` 加減
5. `== != > < >= <=` 比較
6. `not`
7. `and`
8. `or`

---

## 4️⃣ 密碼門檢查（if 判斷式）

```python
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Mary")
elif password == "orion0715":
    print("歡迎orion")
elif password == "abcd":
    print("歡迎Tom")
else:
    print("密碼錯誤")
```

### ✅ 小提醒：

- `if` 只能跑一個符合的條件。
- `elif` 是「否則如果」，當上面條件不成立才會檢查這個。
- `else` 是最後的「都不符合時」。

### ❗ 為什麼不用好幾個 `if`？

如果用很多 `if`，每個都會檢查一遍，浪費時間。
用 `elif` 可以跳過已經符合的條件，更有效率！

---

## 5️⃣ Streamlit 練習（讓 Python 做出網頁！）

### 🔢 數字輸入欄位

```python
st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50)
```

- `step=1.5`：每次加減多少
- `min_value`：最小數
- `max_value`：最大數
- `value`：預設值

---

### 🅰️ 成績等級判斷

```python
a = st.number_input("請輸入成績", step=1, min_value=0, max_value=100, value=50)

if a >= 90:
    st.write("A")
    st.balloons()
elif a >= 80:
    st.write("B")
elif a >= 70:
    st.write("C")
elif a >= 60:
    st.write("D")
else:
    st.write("F")
```

✅ 如果成績在 90 以上，就放氣球！ 🎈

---

## 6️⃣ 按鈕操作（網頁互動功能）

```python
st.button("按我一下", key="button1")
```

- `key`：按鈕的名字（用來區分不同按鈕）

### 🎈 範例：按鈕出現動畫

```python
if st.button("按我一下", key="balloons"):
    st.balloons()

if st.button("按我一下", key="snow"):
    st.snow()
```

- 點擊按鈕可以放氣球 🎈 或下雪 ❄️

---

📌 **結語小提醒**

- `if` 判斷式非常重要，是寫程式邏輯的基礎。
- `and`, `or`, `not` 可以組合條件變更靈活。
- `Streamlit` 是一個超酷的工具，可以讓 Python 做出互動網頁！

---

如果你還有其他上課內容，也可以補充給我，我再幫你一起整理喔 👍

    """
    )
