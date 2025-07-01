import streamlit as st

st.title("奇偶數判斷器")
a = st.number_input("請輸入一個整數", step=1, min_value=0)
if a % 2 == 0:
    st.write(f"{a} 是偶數")
    st.balloons()
else:
    st.write(f"{a} 是奇數")
    st.snow()
