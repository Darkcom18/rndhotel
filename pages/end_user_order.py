import streamlit as st
import uuid
from services.room_service import RoomService
from services.menu_service import MenuService
from services.order_service import OrderService

def render():
    st.title("Đặt món - Khách")

    query_params = st.experimental_get_query_params()
    room_id = query_params.get("room_id",[None])[0]
    if not room_id:
        st.write("Không tìm thấy room_id, vui lòng quét QR hợp lệ!")
        return

    if "end_user_authenticated" not in st.session_state:
        st.session_state["end_user_authenticated"] = None

    if st.session_state["end_user_authenticated"] != room_id:
        pin = st.text_input("Nhập PIN phòng:", type="password")
        if st.button("Xác nhận PIN"):
            r_svc = RoomService()
            if r_svc.check_pin(room_id, pin):
                st.session_state["end_user_authenticated"] = room_id
                st.success("PIN chính xác! Mời bạn đặt món.")
            else:
                st.error("PIN sai!")
        return
    else:
        show_menu(room_id)

def show_menu(room_id):
    from data_access.room_repository import RoomRepository
    room_repo = RoomRepository()
    room = room_repo.get_room_by_id(room_id)
    if not room:
        st.error("Không tìm thấy phòng!")
        return

    workspace_id = room["workspace_id"]
    occupant_name = room.get("occupant_name","")

    menu_svc = MenuService()
    items = menu_svc.get_menu_by_workspace(workspace_id)

    st.subheader("Chọn món")
    selected_ids = []
    for it in items:
        if st.checkbox(f"{it['name']} - {it['price']} VND", key=it["id"]):
            selected_ids.append(it["id"])

    if st.button("Đặt món"):
        if not selected_ids:
            st.warning("Bạn chưa chọn món!")
            return

        total_price = sum([float(x["price"]) for x in items if x["id"] in selected_ids])

        o_svc = OrderService()
        data = {
            "workspace_id": workspace_id,
            "room_id": room_id,
            "occupant_name": occupant_name,
            "items": ",".join(selected_ids),
            "total": total_price,
            "status": "new"
        }
        new_id = o_svc.create_order(data)
        st.success(f"Đặt món thành công! Mã đơn: {new_id}")
