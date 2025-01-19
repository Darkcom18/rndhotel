import uuid
from .base_repository import BaseRepository

class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.ws = self.get_worksheet("MENU")

    def get_menu_by_workspace(self, workspace_id: str):
        rows = self.ws.get_all_records()
        return [r for r in rows if r["workspace_id"] == workspace_id]

    def insert_menu_item(self, data: dict):
        if not data.get("id"):
            data["id"] = str(uuid.uuid4())
        row = [
            data["id"],
            data["workspace_id"],
            data["name"],
            data["price"],
            data.get("description",""),
            data.get("category","")
        ]
        self.ws.append_row(row)
        return data["id"]
