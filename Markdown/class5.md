以下是整理好的 **Python 筆記（高中生版）**，涵蓋今天學到的重點，包括 **字典（dict）**、**Streamlit**、**函式（function）**、**global 變數** 和 **骰子模擬**。

---

# 🧠 Python 筆記整理（高中生版・進階篇）

---

## **一、字典（dict）**

字典（dictionary）是 **鍵值對**（key-value pair）的資料結構，像一個查字典：

```python
d1 = {}  # 空字典
d2 = {"apple": "蘋果"}
d3 = {1: "one", 2: "two", 3: "three"}

print(d2["apple"])  # 輸出 "蘋果"
print(d3[2])        # 輸出 "two"
```

---

### **1. 取得所有 key 或 value**

```python
for key in d3.keys():  # 只取 key
    print(key)

for value in d3.values():  # 只取 value
    print(value)

for key, value in d3.items():  # key 和 value 同時取出
    print(f"{key}: {value}")
```

---

### **2. 新增、修改、刪除**

```python
d3[2] = "二"   # 修改 key=2 的值
d3[4] = "four" # 新增 key=4
print(d3)

v = d3.pop(1)  # 刪除 key=1
print(f"刪除的值: {v}")
```

如果刪除不存在的 key，可以給預設值：

```python
v = d3.pop(5, "不存在的鍵")
print(f"刪除的值: {v}")
```

---

### **3. 其他操作**

```python
print("d3的長度", len(d3))   # 字典長度
print(2 in d3)              # True (檢查 key 是否存在)
print("three" in d3)        # False (值不是 key)
```

---

### **4. List 也可以用 in 檢查**

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("orange" in fruits)  # False
```

---

## **二、Streamlit（互動式網頁工具）**

### **1. 顯示圖片清單**

```python
import streamlit as st
import os

file_path = "image"
files = os.listdir(file_path)  # 取得資料夾內所有檔案
st.write(files)

image_size = st.number_input("圖片大小", min_value=50, max_value=500, value=300, step=50)

for image in files:
    st.image(f"{file_path}/{image}", width=image_size)
```

---

### **2. 購物平台範例**

- 顯示所有商品圖片、價格和庫存
- 支援購買和新增庫存

```python
import streamlit as st
import os
import time

st.title("購物平台")

if "products" not in st.session_state:
    st.session_state.products = {}

col_num = st.number_input("請輸入欄位數", min_value=1, max_value=5, value=3)

file_path = "image"
files = os.listdir(file_path)

# 初始化商品資料
for image in files:
    name = image[:-4]  # 去掉副檔名
    if name not in st.session_state.products:
        st.session_state.products[name] = {"image": f"{file_path}/{image}", "price": 10, "stock": 10}

# 顯示商品
cols = st.columns(col_num)
index = 0
for name, detail in st.session_state.products.items():
    with cols[index % col_num]:
        st.image(detail["image"], use_container_width=True)
        st.write("###", name)
        st.write("價格: $" + str(detail["price"]))
        st.write("庫存: " + str(detail["stock"]))
        if st.button("購買" + name):
            if detail["stock"] > 0:
                st.session_state.products[name]["stock"] -= 1
                st.success(f"已購買{name}")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"{name} 已售完")
                time.sleep(1)
                st.rerun()
        index += 1

# 新增庫存
st.title("新增商品庫存")
col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("請選擇商品", list(st.session_state.products.keys()))
with col2:
    add_num = st.number_input("請輸入庫存數量", min_value=1, max_value=100, value=1)
    if st.button("新增庫存"):
        st.session_state.products[selected_product]["stock"] += add_num
        st.success(f"已新增{add_num}個{selected_product}的庫存")
        time.sleep(1)
        st.rerun()
```

---

## **三、函式（function）**

### **1. 基本函式**

```python
def hello():
    print("hello")

def hello2(name):
    print("hello " + name)
```

---

### **2. 函式回傳值**

```python
def my_max(a, b):
    return a if a > b else b

print(my_max(1, 2))  # 2
```

---

### **3. 預設參數**

```python
def calculate_circle_area(r, pi=3.14, scale=1):
    return pi * (r * scale) ** 2

print(calculate_circle_area(10))               # 314.0
print(calculate_circle_area(10, scale=2))      # 1256.0
print(calculate_circle_area(10, 3.14159, 2))   # 1256.636
```

---

## **四、global 變數**

```python
length = 5
area = 123

def calculate_square_area():
    area = length**2  # 這裡的 area 是區域變數
    print("面積是", area)

def calculate_square_area3():
    global area  # 指定使用全域變數 area
    area = length**2
```

---

## **五、計算兩點距離**

```python
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
```

---

## **六、骰子模擬**

```python
import random

N = int(input("請輸入擲骰子次數： "))
results = []

for i in range(N):
    roll = random.randint(1, 6)
    results.append(roll)

print("所有擲骰子的結果：", results)

# 統計各點數出現次數
n1 = n2 = n3 = n4 = n5 = n6 = 0
for num in results:
    if num == 1: n1 += 1
    elif num == 2: n2 += 1
    elif num == 3: n3 += 1
    elif num == 4: n4 += 1
    elif num == 5: n5 += 1
    else: n6 += 1

print(f"1: {n1}, 2: {n2}, 3: {n3}, 4: {n4}, 5: {n5}, 6: {n6}")
```

---

## **重點總結**

| 主題      | 重點                                            |
| --------- | ----------------------------------------------- |
| dict      | `keys()`, `values()`, `items()`、`pop()`        |
| Streamlit | `st.image()`、`st.button()`、`st.session_state` |
| 函式      | `return`、預設參數、`global`                    |
| 隨機數    | `random.randint(1, 6)`                          |
| 迴圈      | `for ... in ...` 搭配 `if/else`                 |

---

我可以幫你 **把這份筆記排版成 PDF（含程式碼高亮）**，要我幫你生成 PDF 嗎？
