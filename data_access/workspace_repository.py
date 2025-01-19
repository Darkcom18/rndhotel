import uuid
from .base_repository import BaseRepository

class WorkspaceRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.ws = self.get_worksheet("WORKSPACES")

    def get_all_workspaces(self):
        return self.ws.get_all_records()

    def insert_workspace(self, data: dict):
        if not data.get("id"):
            data["id"] = str(uuid.uuid4())
        row = [
            data["id"],
            data["name"],
            data.get("address","")
        ]
        self.ws.append_row(row)
        return data["id"]
