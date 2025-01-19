from data_access.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.repo = UserRepository()

    def login(self, email: str, password: str):
        user_row = self.repo.get_user_by_email(email)
        if user_row and user_row["password"] == password:
            return {
                "id": user_row["id"],
                "email": user_row["email"],
                "name": user_row["name"],
                "role": user_row["role"],
                "workspace_id": user_row["workspace_id"]
            }
        return None
