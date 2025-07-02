import streamlit as st

with st.expander("class2.課堂筆記"):
    st.markdown(
        """

# 🧠 Python 筆記整理（高中生版本）

## 🔹 1. Call by Value vs Call by Reference

### 📌 Call by Value（傳值）

> 適用於數字、字串等簡單型別

```python
a = 1
b = a  # b 拿到 a 的複製品
b = 2
print(a, b)  # 結果：1 2
```

✅ 更改 `b` 不會影響到 `a`，因為兩者儲存在**不同位置**

---

### 📌 Call by Reference（傳參考）

> 適用於 list、dict 等容器型別

```python
a = [1, 2, 3]
b = a  # a 和 b 指向同一個記憶體位置
b[0] = 2
print(a, b)  # 結果： [2, 2, 3] [2, 2, 3]
```

✅ 改變 `b` 的內容，`a` 也會跟著改變！

---

### 🧽 想要避免這種情況，可以使用 `.copy()`

```python
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # 結果： [1, 2, 3] [2, 2, 3]
```

---

## 🔹 2. List 的基本操作

### ➕ append()：在 list 最後加一個元素

```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1, 2, 3, 4]
```

---

### ➖ 刪除元素

#### ✅ remove(值)：刪除第一個出現的指定值

```python
L = ["A", "B", "C", "D", "A"]
L.remove("A")  # 只刪第一個 A
```

🔁 移除全部的 A（不建議這樣寫，會漏掉一些 A）

```python
for i in L:
    if i == "A":
        L.remove(i)
```

#### ✅ pop(index)：刪除指定位置的元素

```python
L = ["A", "B", "C", "D", "A"]
L.pop(0)  # 移除 index 0 的元素（"A"）
L.pop()   # 不指定則移除最後一個元素
```

---

## 🔹 3. List 結構範例

```python
print([])  # 空的 list
print([1, 2, 3])  # 數字 list
print([1, 2, 3, "a", "b", "c"])  # 混合型別
print([1, 2, 3, ["a", "b", "c"]])  # 巢狀 list
print([1, True, "a", 1.23])  # 各種型別混合
```

---

## 🔹 4. List 的資料讀取（用 index）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[3])  # "a"
```

---

## 🔹 5. List 的切片（slice）

### 語法：\[開始:結束:間隔]

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])      # [1, 3, "b"]
print(L[1:4])      # [2, 3, "a"]
print(L[1:4:2])    # [2, "a"]
```

> 切片就像 `range()` 的用法，只是用在 list 上。

---

## 🔹 6. List 的長度

```python
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6（不是最大 index）
```

---

## 🔹 7. List 的走訪（for 迴圈）

### ✅ 用 index 的方式：

```python
L = [1, 2, 3, "a", "b", "c"]
for i in range(len(L)):
    print(L[i])
```

### ✅ 直接取出每個元素：

```python
for i in L:
    print(i)
```

---

## 🔹 8. 實戰範例應用

### ➤ 編號加名字：

```python
name = ["Amy", "Mandy", "Peter"]
for i in range(len(name)):
    print(f"第{i + 1}號是{name[i]}")
```

另一種寫法（但效率較差）：

```python
for i in name:
    a = name.index(i)
    print(f"第{a + 1}號是{i}")
```

---

### ➤ 同時走訪兩個 list：

```python
fruits = ["蘋果", "香蕉", "鳳梨"]
number = [3, 5, 6]

for i in range(len(fruits)):
    print(f"{fruits[i]}有{number[i]}個")
```

---

### ➤ 實作平均值計算

```python
L = [80, 95, 78, 60, 55]
a = L[1]  # 95
L = [64, 73, 52, 34, 95]
b = L[1]  # 73
print((a + b) / 2)  # 84.0
```

---

## 📌 小重點整理

| 主題                  | 說明                              |
| ------------------- | ------------------------------- |
| `a = b`（簡單資料）       | 是複製一份，不會連動（call by value）       |
| `a = b`（list）       | 是共用記憶體，會互相影響（call by reference） |
| `.copy()`           | 複製 list，避免互相影響                  |
| `append()`          | 加元素                             |
| `remove(值)`         | 刪第一個出現的值                        |
| `pop(位置)`           | 刪某個位置的元素                        |
| `len()`             | 算元素總數                           |
| `L[start:end:step]` | 切片取資料                           |


    """
    )

with st.expander("class3.課堂筆記"):
    st.markdown(
        """
# 🧠 Python 筆記整理（高中生版本）

## 🔹 1. Call by Value vs Call by Reference

### 📌 Call by Value（傳值）

> 適用於數字、字串等簡單型別

```python
a = 1
b = a  # b 拿到 a 的複製品
b = 2
print(a, b)  # 結果：1 2
```

✅ 更改 `b` 不會影響到 `a`，因為兩者儲存在**不同位置**

---

### 📌 Call by Reference（傳參考）

> 適用於 list、dict 等容器型別

```python
a = [1, 2, 3]
b = a  # a 和 b 指向同一個記憶體位置
b[0] = 2
print(a, b)  # 結果： [2, 2, 3] [2, 2, 3]
```

✅ 改變 `b` 的內容，`a` 也會跟著改變！

---

### 🧽 想要避免這種情況，可以使用 `.copy()`

```python
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # 結果： [1, 2, 3] [2, 2, 3]
```

---

## 🔹 2. List 的基本操作

### ➕ append()：在 list 最後加一個元素

```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1, 2, 3, 4]
```

---

### ➖ 刪除元素

#### ✅ remove(值)：刪除第一個出現的指定值

```python
L = ["A", "B", "C", "D", "A"]
L.remove("A")  # 只刪第一個 A
```

🔁 移除全部的 A（不建議這樣寫，會漏掉一些 A）

```python
for i in L:
    if i == "A":
        L.remove(i)
```

#### ✅ pop(index)：刪除指定位置的元素

```python
L = ["A", "B", "C", "D", "A"]
L.pop(0)  # 移除 index 0 的元素（"A"）
L.pop()   # 不指定則移除最後一個元素
```

---

## 🔹 3. List 結構範例

```python
print([])  # 空的 list
print([1, 2, 3])  # 數字 list
print([1, 2, 3, "a", "b", "c"])  # 混合型別
print([1, 2, 3, ["a", "b", "c"]])  # 巢狀 list
print([1, True, "a", 1.23])  # 各種型別混合
```

---

## 🔹 4. List 的資料讀取（用 index）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[3])  # "a"
```

---

## 🔹 5. List 的切片（slice）

### 語法：\[開始:結束:間隔]

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])      # [1, 3, "b"]
print(L[1:4])      # [2, 3, "a"]
print(L[1:4:2])    # [2, "a"]
```

> 切片就像 `range()` 的用法，只是用在 list 上。

---

## 🔹 6. List 的長度

```python
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6（不是最大 index）
```

---

## 🔹 7. List 的走訪（for 迴圈）

### ✅ 用 index 的方式：

```python
L = [1, 2, 3, "a", "b", "c"]
for i in range(len(L)):
    print(L[i])
```

### ✅ 直接取出每個元素：

```python
for i in L:
    print(i)
```

---

## 🔹 8. 實戰範例應用

### ➤ 編號加名字：

```python
name = ["Amy", "Mandy", "Peter"]
for i in range(len(name)):
    print(f"第{i + 1}號是{name[i]}")
```

另一種寫法（但效率較差）：

```python
for i in name:
    a = name.index(i)
    print(f"第{a + 1}號是{i}")
```

---

### ➤ 同時走訪兩個 list：

```python
fruits = ["蘋果", "香蕉", "鳳梨"]
number = [3, 5, 6]

for i in range(len(fruits)):
    print(f"{fruits[i]}有{number[i]}個")
```

---

### ➤ 實作平均值計算

```python
L = [80, 95, 78, 60, 55]
a = L[1]  # 95
L = [64, 73, 52, 34, 95]
b = L[1]  # 73
print((a + b) / 2)  # 84.0
```

---

## 📌 小重點整理

| 主題                | 說明                                          |
| ------------------- | --------------------------------------------- |
| `a = b`（簡單資料） | 是複製一份，不會連動（call by value）         |
| `a = b`（list）     | 是共用記憶體，會互相影響（call by reference） |
| `.copy()`           | 複製 list，避免互相影響                       |
| `append()`          | 加元素                                        |
| `remove(值)`        | 刪第一個出現的值                              |
| `pop(位置)`         | 刪某個位置的元素                              |
| `len()`             | 算元素總數                                    |
| `L[start:end:step]` | 切片取資料                                    |

"""
    )
