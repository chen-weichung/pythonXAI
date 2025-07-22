# import streamlit as st

# st.write("輸入成績")
# a = st.number_input("輸入你的成績", step=1, min_value=0, max_value=100)
# if a >= 90:
#     st.write("A")
# elif a >= 80:
#     st.write("B")
# elif a >= 70:
#     st.write("C")
# elif a >= 60:
#     st.write("D")
# else:
#     st.write("F")

import streamlit as st

st.write("請輸入一個數字")
a = st.number_input("請輸入一個整數", step=1, min_value=0)
total = ""
for i in range(1, a + 1):
    c = " " * (a - i)
    d = "*" * (2 * i - 1)
    total += f"{c}{d}\n"
for i in range(1, a + 1):
    e = " " * (a - 1) + "*"
    total += f"{e}\n"
    st.markdown(f"```\n{total}```")
# \n是換行
