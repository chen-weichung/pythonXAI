# print([])  # 這是一個空的list
# print([1, 2, 3])  # 這是一個有三個元素的list
# print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的list
# print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有四個元素的list
# print([1, True, "a", 1.23])  # 這是一個有四個元素的list

# # list 讀取元素，元素的index從0開始
# L = [1, 2, 3, "a", "b", "c"]
# print(L[0])  # 1
# print(L[1])  # 2
# print(L[2])  # 3
# print(L[3])  # "a"

L = [80, 95, 78, 60, 55]
a = L[1]  # 95
L = [64, 73, 52, 34, 95]
b = L[1]  # 73
print((a + b) / 2)  # 84.0

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取2個元素所以是[1,3,"b"]
print(L[::2])
# 就是取index1-3的元素，不包含index 4，所以是[2,3,"a"]
print(L[1:4])
# 就是取index1-3的元素，不包含index 4，並且每次取2個元素，所以是[2,"a"]
print(L[1:4:2])
# 跟range 一樣的用法，只是符號不同

# list取長度，也就是list裡面有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取的資料
# 這兩種方式都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]
for i in range(len(L)):
    print(L[i])
for i in L:
    print(i)


name = ["Amy", "Mandy", "Peter"]
for i in range(len(name)):
    print(f"第{i + 1}號是{name[i]}")

for i in name:
    a = name.index(i)
    print(f"第{a+1}號是{i}")
