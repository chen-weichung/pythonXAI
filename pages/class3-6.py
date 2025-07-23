import random
import streamlit as st

# # target = random.randint(1, 100)
# # st.write(target)
# # while True:
# #     guess = st.number_input("請輸入一個數字:", min_value=0, max_value=100)
# #     if guess < target:
# #         st.write("再大一點")
# #     elif guess > target:
# #         st.write("在小一點")
# #     else:
# #         st.write("猜中了")
# #         break

# if "target" not in st.session_state:
#     st.session_state.target = random.randint(1, 100)
# if "message" not in st.session_state:
#     st.session_state.message = ""

# guess = st.number_input("請輸入一個數字:", min_value=0, max_value=100, key="guess")
# if st.button("猜！"):
#     if guess < st.session_state.target:
#         st.session_state.message = "再大一點"
#     elif guess > st.session_state.target:
#         st.session_state.message = "在小一點"
#     else:
#         st.session_state.message = "猜中了"
# st.write(st.session_state.message)

tatal = []
for i in range(100):
    tatal.append(0)
target = random.randint(1, 100)
tatal[target - 1] = 1

count = 0
while True:
    pick = random.randint(1, 100)
    count += 1
    if tatal[pick - 1] == 2:
        print(f"已經抽過了")
        count -= 1
    elif tatal[pick - 1] == 1:
        print(f"恭喜中獎")
        break
    else:
        print(f"沒有中獎，繼續抽")
    tatal[pick - 1] = 2
print(f"總共抽了{count}次，花費{count*200}元")
