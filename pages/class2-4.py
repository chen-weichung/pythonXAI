import streamlit as st

st.title("練習：for 迴圈")
st.write("請輸入一個數字(1-9)")
a = st.number_input("請輸入一個整數", step=1, min_value=0, max_value=9)
for i in range(a + 1):
    st.write(f"{i*str(i)}")
