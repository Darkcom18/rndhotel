import streamlit as st
from services.room_service import RoomService

def render():
    st.title("Quản lý Phòng & PIN")

    user = st.session_state["user"]
    ws_id = user["workspace_id"]
    room_svc = RoomService()

    rooms = room_svc.get_rooms_by_workspace(ws_id)
    st.subheader("Danh sách phòng")
    for r in rooms:
        st.write(f"Phòng: {r['room_number']} - PIN: {r['pin']} - Khách: {r['occupant_name']}")

    st.subheader("Thêm/Update phòng")
    room_number = st.text_input("Số phòng:")
    pin = st.text_input("PIN:")
    occupant_name = st.text_input("Tên khách:")
    occupant_phone = st.text_input("SĐT khách:")

    if st.button("Lưu phòng"):
        data = {
            "id": "",
            "workspace_id": ws_id,
            "room_number": room_number,
            "pin": pin,
            "occupant_name": occupant_name,
            "occupant_phone": occupant_phone
        }
        room_id = room_svc.save_room(data)
        st.success(f"Đã lưu phòng, ID = {room_id}")
        st.experimental_rerun()
