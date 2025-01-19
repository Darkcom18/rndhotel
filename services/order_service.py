from data_access.order_repository import OrderRepository

class OrderService:
    def __init__(self):
        self.repo = OrderRepository()

    def create_order(self, data: dict):
        return self.repo.insert_order(data)

    def get_orders_by_workspace(self, workspace_id: str):
        return self.repo.get_orders_by_workspace(workspace_id)

    def update_order_status(self, order_id: str, new_status: str):
        return self.repo.update_order_status(order_id, new_status)
