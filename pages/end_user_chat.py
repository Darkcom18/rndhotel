import streamlit as st
from services.room_service import RoomService
from services.chat_log_service import ChatLogService
from services.chat_service import ChatService

def render():
    st.title("Chat với Nhân Viên (End-user)")

    query_params = st.experimental_get_query_params()
    room_id = query_params.get("room_id",[None])[0]
    if not room_id:
        st.write("Không thấy room_id, quét lại QR!")
        return

    if "end_user_chat_authenticated" not in st.session_state:
        st.session_state["end_user_chat_authenticated"] = None

    if st.session_state["end_user_chat_authenticated"] != room_id:
        pin = st.text_input("Nhập PIN phòng:", type="password")
        if st.button("Xác nhận PIN"):
            r_svc = RoomService()
            if r_svc.check_pin(room_id, pin):
                st.session_state["end_user_chat_authenticated"] = room_id
                st.success("PIN chính xác, mời bạn trò chuyện!")
            else:
                st.error("PIN sai!")
        return
    else:
        show_chat_ui(room_id)

def show_chat_ui(room_id):
    chatlog_svc = ChatLogService()
    chat_svc = ChatService()

    logs = chatlog_svc.get_logs_by_room(room_id)
    for log in logs:
        st.write(f"{log['timestamp']} - {log['sender_role']}: {log['message']}")

    new_msg = st.text_input("Nội dung chat:")
    if st.button("Gửi"):
        # Lưu tin end_user
        chatlog_svc.insert_log({
            "workspace_id": "",
            "room_id": room_id,
            "sender_role": "end_user",
            "message": new_msg
        })
        # Gọi AI (nếu muốn)
        reply = chat_svc.send_message_to_coze(new_msg, {"room_id": room_id})
        chatlog_svc.insert_log({
            "workspace_id": "",
            "room_id": room_id,
            "sender_role": "assistant",
            "message": reply
        })
        st.experimental_rerun()
