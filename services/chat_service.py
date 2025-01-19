import requests
from core.config import Config

class ChatService:
    def __init__(self):
        self.api_key = Config.get_coze_api_key()
        self.endpoint = Config.get_coze_endpoint()

    def send_message_to_coze(self, message: str, context: dict=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "message": message,
            "context": context
        }
        try:
            resp = requests.post(self.endpoint, json=payload, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return data.get("reply","")
            else:
                return f"Error {resp.status_code} from Coze AI"
        except Exception as e:
            return f"Lỗi: {str(e)}"
