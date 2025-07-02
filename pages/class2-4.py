# import streamlit as st

# st.title("練習：for 迴圈")
# st.write("請輸入一個數字(1-9)")
# a = st.number_input("請輸入一個整數", step=1, min_value=0, max_value=9)
# for i in range(a + 1):
#     st.write(f"{i*str(i)}")

import streamlit as st

st.title("練習：for 迴圈")
st.write("請輸入一個數字")
a = st.number_input("請輸入一個整數", step=1, min_value=0, max_value=5)
total = ""
for i in range(1, a + 1):
    c = " " * (a - i)
    d = "*" * (2 * i - 1)
    total += f"{c}{d}\n"
for i in range(1, a + 1):
    e = " " * (a - 1) + "*"
    total += f"{e}\n"
st.markdown(f"```\n{total}```")
