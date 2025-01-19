import uuid
from .base_repository import BaseRepository

class RoomRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.ws = self.get_worksheet("ROOMS")

    def get_room_by_id(self, room_id: str):
        rows = self.ws.get_all_records()
        for r in rows:
            if r["id"] == room_id:
                return r
        return None

    def get_rooms_by_workspace(self, workspace_id: str):
        rows = self.ws.get_all_records()
        return [r for r in rows if r["workspace_id"] == workspace_id]

    def insert_or_update_room(self, data: dict):
        rows = self.ws.get_all_records()
        if not data.get("id"):
            data["id"] = str(uuid.uuid4())
            row = [
                data["id"],
                data["workspace_id"],
                data["room_number"],
                data.get("pin",""),
                data.get("occupant_name",""),
                data.get("occupant_phone","")
            ]
            self.ws.append_row(row)
            return data["id"]
        else:
            # Update
            for i, r in enumerate(rows):
                if r["id"] == data["id"]:
                    row_index = i+2
                    self.ws.update_cell(row_index, 2, data["workspace_id"])
                    self.ws.update_cell(row_index, 3, data["room_number"])
                    self.ws.update_cell(row_index, 4, data.get("pin",""))
                    self.ws.update_cell(row_index, 5, data.get("occupant_name",""))
                    self.ws.update_cell(row_index, 6, data.get("occupant_phone",""))
                    return data["id"]
            # Nếu k tìm thấy => append
            data["id"] = str(uuid.uuid4())
            row = [
                data["id"],
                data["workspace_id"],
                data["room_number"],
                data.get("pin",""),
                data.get("occupant_name",""),
                data.get("occupant_phone","")
            ]
            self.ws.append_row(row)
            return data["id"]
