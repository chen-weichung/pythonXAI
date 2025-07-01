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
