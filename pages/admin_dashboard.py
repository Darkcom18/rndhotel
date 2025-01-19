import streamlit as st
from data_access.user_repository import UserRepository
from core.constants import Role

def render():
    st.title("Site Admin Dashboard")

    st.subheader("Tạo user mới (VD: Manager)")
    email = st.text_input("Email:")
    password = st.text_input("Password:")
    name = st.text_input("Tên:")
    role = st.selectbox("Role", [Role.MANAGER, Role.LETAN, Role.STAFF])
    workspace_id = st.text_input("Workspace ID (VD: hotelB, resortA)")

    if st.button("Tạo User"):
        user_repo = UserRepository()
        data = {
            "email": email,
            "password": password,
            "name": name,
            "role": role,
            "workspace_id": workspace_id
        }
        new_id = user_repo.insert_user(data)
        st.success(f"User created: {new_id}")
