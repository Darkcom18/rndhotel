from data_access.chatlog_repository import ChatLogRepository

class ChatLogService:
    def __init__(self):
        self.repo = ChatLogRepository()

    def insert_log(self, data: dict):
        return self.repo.insert_chatlog(data)

    def get_logs_by_workspace(self, workspace_id: str):
        return self.repo.get_chatlogs_by_workspace(workspace_id)

    def get_logs_by_room(self, room_id: str):
        return self.repo.get_chatlogs_by_room(room_id)
