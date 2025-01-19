import gspread
from google.oauth2.service_account import Credentials
from core.config import Config

class BaseRepository:
    def __init__(self):
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        service_account_info = Config.get_service_account_dict()
        credentials = Credentials.from_service_account_info(service_account_info, scopes=scopes)

        self.gc = gspread.authorize(credentials)

        # Dùng open_by_key (theo ID)
        sheet_id = Config.get_gspread_sheet_id()
        self.sheet_file = self.gc.open_by_key(sheet_id)

    def get_worksheet(self, name: str):
        return self.sheet_file.worksheet(name)
