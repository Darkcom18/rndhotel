import streamlit as st
from services.order_service import OrderService
from core.constants import OrderStatus

def render():
    st.title("Quản lý Orders")

    user = st.session_state["user"]
    ws_id = user["workspace_id"]

    order_svc = OrderService()
    orders = order_svc.get_orders_by_workspace(ws_id)

    for o in orders:
        st.write(f"Order ID: {o['id']} - Phòng: {o['room_id']} - Khách: {o['occupant_name']}")
        st.write(f"Món: {o['items']} - Tổng: {o['total']} - Trạng thái: {o['status']}")
        new_status = st.selectbox("Trạng thái", 
            [OrderStatus.NEW, OrderStatus.CONFIRMED, OrderStatus.COMPLETED, OrderStatus.CANCELLED],
            index=[OrderStatus.NEW,OrderStatus.CONFIRMED,OrderStatus.COMPLETED,OrderStatus.CANCELLED].index(o['status']),
            key=o['id'])
        if st.button(f"Update {o['id']}"):
            order_svc.update_order_status(o["id"], new_status)
            st.success("Đã cập nhật!")
            st.experimental_rerun()
