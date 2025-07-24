def hello():
    print("hello")


def hello2(name):
    print("hello " + name)


def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def calculate_circle_area(r, pi=3.14, scale=1):
    return pi * (r * scale) ** 2


hello()
hello2("Mike")
print(my_max(1, 2))
print(calculate_circle_area(10))
print(calculate_circle_area(10, scale=2))
print(calculate_circle_area(10, 3.14159, 2))

print("-" * 20)

length = 5
area = 123


def calculate_square_area():
    # print("面積是", area)#會報錯
    area = length**2
    print("面積是", area)


def calculate_square_area2():
    area = length**2
    return area


def calculate_square_area3():
    global area
    area = length**2


length = 10
calculate_square_area()
print(calculate_square_area2())
calculate_square_area3()
print(area)

print("-" * 20)


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1 = int(input("請輸入x1:"))
y1 = int(input("請輸入y1:"))
x2 = int(input("請輸入x2:"))
y2 = int(input("請輸入y2:"))
print(distance(x1, y1, x2, y2))

import random

N = int(input("請輸入擲骰子次數： "))

results = []

for i in range(N):
    roll = random.randint(1, 6)
    results.append(roll)
print("所有擲骰子的結果：", results)

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
for num in results:
    if num == 1:
        n1 += 1
    elif num == 2:
        n2 += 1
    elif num == 3:
        n3 += 1
    elif num == 4:
        n4 += 1
    elif num == 5:
        n5 += 1
    else:
        n6 += 1
print(f"1: {n1}, 2: {n2}, 3: {n3}, 4: {n4}, 5: {n5}, 6: {n6}")
