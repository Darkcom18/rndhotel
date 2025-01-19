from data_access.menu_repository import MenuRepository

class MenuService:
    def __init__(self):
        self.repo = MenuRepository()

    def get_menu_by_workspace(self, workspace_id: str):
        return self.repo.get_menu_by_workspace(workspace_id)

    def create_menu_item(self, data: dict):
        return self.repo.insert_menu_item(data)
