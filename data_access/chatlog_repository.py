import uuid
from datetime import datetime
from .base_repository import BaseRepository

class ChatLogRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.ws = self.get_worksheet("CHATLOGS")

    def insert_chatlog(self, data: dict):
        """
        data = {
          "workspace_id": ...,
          "room_id": ...,
          "sender_role": ...,
          "message": ...,
          "timestamp": ...
        }
        """
        if not data.get("id"):
            data["id"] = str(uuid.uuid4())
        if not data.get("timestamp"):
            data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = [
            data["id"],
            data.get("workspace_id",""),
            data.get("room_id",""),
            data["sender_role"],
            data["message"],
            data["timestamp"]
        ]
        self.ws.append_row(row)
        return data["id"]

    def get_chatlogs_by_workspace(self, workspace_id: str):
        rows = self.ws.get_all_records()
        return [r for r in rows if r["workspace_id"] == workspace_id]

    def get_chatlogs_by_room(self, room_id: str):
        rows = self.ws.get_all_records()
        return [r for r in rows if r["room_id"] == room_id]
