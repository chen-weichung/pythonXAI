# # import streamlit as st

# # st.title("奇偶數判斷器")
# # a = st.number_input("請輸入一個整數", step=1, min_value=0)
# # if a % 2 == 0:
# #     st.write(f"{a} 是偶數")
# #     st.balloons()
# # else:
# #     st.write(f"{a} 是奇數")
# #     st.snow()

# # for 迴圈
# # for會搭配in來使用，in 後面接著一個有範圍的東西
# # range(5)會產生 0, 1, 2, 3, 4，不包含5
# # i是迴圈數的變數可以自己命名
# # 迴圈變數每回合會從範圍面取一個變數出來
# for i in range(5):
#     print(i, end=" ")
# # range可以設定起始值和結束值，但部會包含結束值
# # range(1,5)會產生 1, 2, 3, 4
# for i in range(1, 5):
#     print(i, end=",")
# # range可以設定起始值、結束值和間隔值，但不會包含結束值
# # range(1,10,2)會產生 1, 3, 5, 7, 9
# for i in range(1, 10, 2):
#     print(i, end=",")

# import streamlit as st

# st.title("練習：for 迴圈")
# st.write("請輸入兩個數字")
# b = st.number_input("請輸入起始值", step=1)
# a = st.number_input("請輸入結束值", step=1)

# for i in range(b, a + 1):
#     st.write(f"{i}號在教室", end=",")

import streamlit as st

st.title("練習：for 迴圈")
st.write("請輸入兩個數字")
b = st.number_input("請輸入起始值", step=1)
a = st.number_input("請輸入結束值", step=1)
total = 0
for i in range(b, a + 1):
    total += i
st.write(f"{b}到{a}的總和是{total}")
