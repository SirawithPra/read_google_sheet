import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import streamlit as st

# SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'keys.json'

cred = None
cred = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#https://docs.google.com/spreadsheets/d/1q7I3Gw6wyEdsOxO1cMkVdFVT8Zq54CRNKNuhEtc2GdA/edit#gid=527336470
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1q7I3Gw6wyEdsOxO1cMkVdFVT8Zq54CRNKNuhEtc2GdA"
SAMPLE_RANGE_NAME = "test!A1:H"


service = build("sheets", "v4", credentials=cred)

# Call the Sheets API
sheet = service.spreadsheets()
result = (sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                             range=SAMPLE_RANGE_NAME).execute())
values = result.get("values", [])

df= pd.DataFrame(values)
st.write('บันทึกลงระบบเรียบร้อย')
st.table(df)

df.isna()