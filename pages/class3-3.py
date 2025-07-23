import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")

col3, col4, col5 = st.columns([1, 2, 3])
with col3:
    st.write("欄位3")
    st.write("按鈕3")
with col4:
    st.write("欄位4")
    st.write("按鈕4")
with col5:
    st.write("欄位5")
    st.write("按鈕5")
