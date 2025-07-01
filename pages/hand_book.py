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
