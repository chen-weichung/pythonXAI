# import streamlit as st

# number = st.number_input("請輸入一個數字", step=1.5, min_value=-12.5, max_value=100.0)
# # step=1 表示單位以及每次增加或減少的數量，min_value 表示最小值，max_value 表示最大值
# st.write(f"你輸入的數字是: {number}")

import streamlit as st

st.title("練習")
st.write("輸入成績")
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
    st.snow()

import streamlit as st

st.markdown("---")
st.markdown("## 按鈕範例")
# st.button("按鈕") 可以在網頁上顯示一個按鈕，使用者可以點擊按鈕
# key是按鈕的識別名稱，可以用來區分不同的按鈕
# 如果使用者點擊按鈕，st.button() 會回傳 True，否則回傳 False
st.button("按我一下", key="button1")
if st.button("按我一下", key="balloons"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
st.markdown("---")
