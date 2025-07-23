import streamlit as st

st.title("點餐機")
food = st.text_input("請輸入餐點")
st.title("購物籃")
st.write("購物籃")
col1, col2 = st.columns(2)
col1.button("加入")
col2.button("移除")
