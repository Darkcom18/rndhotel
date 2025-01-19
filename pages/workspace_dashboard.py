import streamlit as st
from services.order_service import OrderService

def render():
    st.title("Workspace Dashboard")
    user = st.session_state["user"]
    ws_id = user["workspace_id"]

    order_svc = OrderService()
    orders = order_svc.get_orders_by_workspace(ws_id)
    st.write(f"Tổng đơn hàng: {len(orders)}")
    # Bạn có thể thêm chart, statistic...
