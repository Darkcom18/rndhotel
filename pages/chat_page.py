import streamlit as st
from services.chat_log_service import ChatLogService
from services.chat_service import ChatService

def render():
    st.title("Chat Nội Bộ")
    user = st.session_state["user"]
    workspace_id = user["workspace_id"]
    sender_role = user["role"]

    chatlog_svc = ChatLogService()
    chat_svc = ChatService()

    # Lấy tất cả logs workspace
    logs = chatlog_svc.get_logs_by_workspace(workspace_id)
    # Hiển thị
    for log in logs:
        st.write(f"{log['timestamp']} - {log['sender_role']}: {log['message']}")

    new_msg = st.text_input("Nhập tin nhắn:")
    if st.button("Gửi"):
        # Lưu tin user
        chatlog_svc.insert_log({
            "workspace_id": workspace_id,
            "room_id": "",
            "sender_role": sender_role,
            "message": new_msg
        })
        # Gọi Coze AI
        reply = chat_svc.send_message_to_coze(new_msg, {"workspace_id": workspace_id})
        # Lưu tin AI
        chatlog_svc.insert_log({
            "workspace_id": workspace_id,
            "room_id": "",
            "sender_role": "assistant",
            "message": reply
        })
        st.experimental_rerun()
