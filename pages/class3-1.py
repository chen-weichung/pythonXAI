# call by value
a = 1
b = a  # b是a的複製品
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b，但是b跟a指向不同記憶體位置
b[0] = 2
print(a, b)

# list的append跟
L = [1, 2, 3]
L.append(4)  # 在list的最後面加上4
print(L)

# list的移除元素方式有兩種
# 1. 使用remove，可以移除指定的元素
L = ["A", "B", "C", "D", "A"]
L.remove("A")  # 移除第一個出現的"A"
# 代表remove會從頭開始找，找到第一個符合的元素就會移除
# 如果想要移除所有符合的元素，可以使用迴圈
for i in L:
    if i == "A":
        L.remove(i)
# 2. 使用pop，可以移除指定的index位置的元素
L = ["A", "B", "C", "D", "A"]
L.pop(0)  # 移除index為0的元素
# 代表pop會移除指定的index位置的元素
# 如果不指定index，則會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)
# 3使用sort由小至大排列元素
L = [5, 3, 8, 6, 7, 1, 9, 4]
L.sort()
print(L)
