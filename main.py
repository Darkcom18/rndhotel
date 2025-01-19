import streamlit as st
from services.auth_service import AuthService
from pages import (
    admin_dashboard,
    workspace_dashboard,
    rooms_page,
    menu_page,
    orders_page,
    chat_page,
    end_user_order,
    end_user_chat
)
from core.constants import Role

def main():
    st.set_page_config(page_title="Hotel Platform", layout="wide")

    # Kiểm tra query param ?page=end_user_order / end_user_chat
    query_params = st.experimental_get_query_params()
    page_param = query_params.get("page", [None])[0]

    # Nếu end-user truy cập trang đặt món
    if page_param == "end_user_order":
        end_user_order.render()
        return

    # Nếu end-user truy cập trang chat
    elif page_param == "end_user_chat":
        end_user_chat.render()
        return

    # Nếu không phải end-user => logic đăng nhập nhân viên/manager/site_admin
    if "user" not in st.session_state:
        st.session_state["user"] = None

    # Kiểm tra trạng thái đăng nhập
    if st.session_state["user"] is None:
        show_login()
    else:
        show_dashboard()

def show_login():
    st.title("Login (Admin / Manager / Lễ tân / Staff)")
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")
    if st.button("Đăng nhập"):
        auth = AuthService()
        user = auth.login(email, password)
        if user:
            st.session_state["user"] = user
            st.experimental_rerun()
        else:
            st.error("Sai email hoặc password!")

def show_dashboard():
    user = st.session_state["user"]
    role = user["role"]

    if role == Role.SITE_ADMIN:
        show_site_admin_layout()
    elif role == Role.MANAGER:
        show_manager_layout()
    elif role == Role.LETAN:
        show_letan_layout()
    elif role == Role.STAFF:
        show_staff_layout()
    else:
        st.error(f"Role không được hỗ trợ: {role}")

def show_site_admin_layout():
    st.sidebar.title("Site Admin Menu")
    choice = st.sidebar.selectbox("Điều hướng", ["Admin Dashboard", "Chat", "Đăng xuất"])
    if choice == "Admin Dashboard":
        admin_dashboard.render()
    elif choice == "Chat":
        chat_page.render()
    elif choice == "Đăng xuất":
        do_logout()

def show_manager_layout():
    """Manager có toàn quyền trong workspace: rooms, menu, orders, chat, dashboard..."""
    st.sidebar.title("Manager Menu")
    choice = st.sidebar.selectbox("Điều hướng", 
        ["Dashboard", "Quản lý Phòng", "Quản lý Menu", "Quản lý Orders", "Chat", "Đăng xuất"]
    )
    if choice == "Dashboard":
        workspace_dashboard.render()
    elif choice == "Quản lý Phòng":
        rooms_page.render()
    elif choice == "Quản lý Menu":
        menu_page.render()
    elif choice == "Quản lý Orders":
        orders_page.render()
    elif choice == "Chat":
        chat_page.render()
    elif choice == "Đăng xuất":
        do_logout()

def show_letan_layout():
    """
    Lễ tân có thể: xem dashboard, quản lý orders (tiếp nhận, confirm), 
    phòng (nếu muốn), chat...
    """
    st.sidebar.title("Lễ tân Menu")
    choice = st.sidebar.selectbox("Điều hướng",
        ["Dashboard", "Quản lý Phòng", "Quản lý Orders", "Chat", "Đăng xuất"]
    )
    if choice == "Dashboard":
        workspace_dashboard.render()
    elif choice == "Quản lý Phòng":
        # Nếu bạn cho phép lễ tân cập nhật pin phòng, occupant_name...
        rooms_page.render()
    elif choice == "Quản lý Orders":
        orders_page.render()
    elif choice == "Chat":
        chat_page.render()
    elif choice == "Đăng xuất":
        do_logout()

def show_staff_layout():
    """
    Nhân viên nhà hàng/bar (staff) có thể: tạo menu, xem orders, chat...
    Tuỳ nhu cầu thực tế, bạn có thể cho staff xem dashboard, 
    hoặc giới hạn, v.v.
    """
    st.sidebar.title("Staff Menu")
    choice = st.sidebar.selectbox("Điều hướng",
        ["Quản lý Menu", "Quản lý Orders", "Chat", "Đăng xuất"]
    )
    if choice == "Quản lý Menu":
        menu_page.render()
    elif choice == "Quản lý Orders":
        orders_page.render()
    elif choice == "Chat":
        chat_page.render()
    elif choice == "Đăng xuất":
        do_logout()

def do_logout():
    st.session_state["user"] = None
    st.experimental_rerun()

if __name__ == "__main__":
    main()
