import streamlit as st
import json

class Config:
    @staticmethod
    def get_service_account_dict():
        # Lấy dict JSON từ secrets
        return json.loads(st.secrets["gcp"]["service_account_json"])

    @staticmethod
    def get_gspread_sheet_name():
        return st.secrets["gcp"]["gspread_sheet_name"]

    @staticmethod
    def get_coze_api_key():
        return st.secrets["coze"]["api_key"]

    @staticmethod
    def get_coze_endpoint():
        return st.secrets["coze"]["endpoint"]
