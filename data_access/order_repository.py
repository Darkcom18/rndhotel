import uuid
from datetime import datetime
from .base_repository import BaseRepository

class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.ws = self.get_worksheet("ORDERS")

    def insert_order(self, data: dict):
        if not data.get("id"):
            data["id"] = str(uuid.uuid4())
        if not data.get("created_at"):
            data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = [
            data["id"],
            data["workspace_id"],
            data["room_id"],
            data.get("occupant_name",""),
            data["items"],
            data.get("total",0),
            data.get("status","new"),
            data["created_at"]
        ]
        self.ws.append_row(row)
        return data["id"]

    def get_orders_by_workspace(self, workspace_id: str):
        rows = self.ws.get_all_records()
        return [r for r in rows if r["workspace_id"] == workspace_id]

    def update_order_status(self, order_id: str, new_status: str):
        rows = self.ws.get_all_records()
        for i, r in enumerate(rows):
            if r["id"] == order_id:
                row_index = i + 2
                self.ws.update_cell(row_index, 7, new_status)
                return True
        return False
