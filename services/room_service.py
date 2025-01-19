from data_access.room_repository import RoomRepository

class RoomService:
    def __init__(self):
        self.repo = RoomRepository()

    def get_rooms_by_workspace(self, workspace_id: str):
        return self.repo.get_rooms_by_workspace(workspace_id)

    def save_room(self, data: dict):
        return self.repo.insert_or_update_room(data)

    def check_pin(self, room_id: str, pin: str):
        room = self.repo.get_room_by_id(room_id)
        if room and str(room["pin"]) == pin:
            return True
        return False
