import streamlit as st
import json

class Config:
    @staticmethod
    def get_service_account_dict():
        return json.loads(st.secrets["gcp"]["service_account_json"])

    @staticmethod
    def get_gspread_sheet_id():
        # Lấy ID (VD: "19J0U3CfZjqG5cN_J0nmNP8E2Z7qEyZrt4GrhzBqGTUI")
        return st.secrets["gcp"]["gspread_sheet_id"]

    @staticmethod
    def get_coze_api_key():
        return st.secrets["coze"]["api_key"]

    @staticmethod
    def get_coze_endpoint():
        return st.secrets["coze"]["endpoint"]
