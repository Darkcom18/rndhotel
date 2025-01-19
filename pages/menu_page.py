import streamlit as st
from services.menu_service import MenuService

def render():
    st.title("Quản lý Menu")

    user = st.session_state["user"]
    ws_id = user["workspace_id"]

    menu_svc = MenuService()
    items = menu_svc.get_menu_by_workspace(ws_id)

    st.subheader("Menu hiện tại")
    for m in items:
        st.write(f"- {m['name']} ({m['price']} đ) - {m['description']}")

    st.subheader("Thêm món mới")
    name = st.text_input("Tên món:")
    price = st.number_input("Giá:", min_value=0, step=1000)
    desc = st.text_input("Mô tả:")

    if st.button("Thêm"):
        data = {
            "workspace_id": ws_id,
            "name": name,
            "price": price,
            "description": desc
        }
        new_id = menu_svc.create_menu_item(data)
        st.success(f"Đã thêm món. ID={new_id}")
        st.experimental_rerun()
