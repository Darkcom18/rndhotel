import uuid
from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.ws = self.get_worksheet("USERS")

    def get_user_by_email(self, email: str):
        rows = self.ws.get_all_records()
        for r in rows:
            if r["email"] == email:
                return r
        return None

    def insert_user(self, data: dict):
        if "id" not in data or not data["id"]:
            data["id"] = str(uuid.uuid4())
        row = [
            data["id"],
            data["email"],
            data["password"],
            data["name"],
            data["role"],
            data.get("workspace_id","")
        ]
        self.ws.append_row(row)
        return data["id"]
