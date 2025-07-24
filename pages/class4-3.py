import streamlit as st
import os
import time

st.title("購物平台")

if "products" not in st.session_state:
    st.session_state.products = {}

col_num = st.number_input("請輸入欄位數", min_value=1, max_value=5, value=3, step=1)

file_path = "image"
files = os.listdir(file_path)

for image in files:
    name = image[:-4]
    if name not in st.session_state.products:
        st.session_state.products[name] = {
            "image": f"{file_path}/{image}",
            "price": 10,
            "stock": 10,
        }

cols = st.columns(col_num)

index = 0
for name, detail in st.session_state.products.items():
    with cols[index % col_num]:
        st.image(detail["image"], use_container_width=True)
        st.write("###", name)
        st.write("價格: $" + str(detail["price"]))
        st.write("庫存: " + str(detail["stock"]))
        if st.button("購買" + name):
            if detail["stock"] > 0:
                st.session_state.products[name]["stock"] -= 1
                st.success(f"已購買{name}")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"{name} 已售完")
                time.sleep(1)
                st.rerun()
        index += 1
st.title
