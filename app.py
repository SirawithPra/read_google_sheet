import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# กำหนดขอบเขตของการใช้งาน (Scope)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# โหลดไฟล์ข้อมูล Credential JSON ที่ได้รับจากการสร้างโปรเจกต์ใน Google Cloud Platform
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# ติดต่อ Google Sheets API
gc = gspread.authorize(credentials)

# เปิด Google Sheets ด้วยชื่อไฟล์หรือ ID ของ Google Sheets
sheet = gc.open_by_key('1rrdzFjxheFK5MiJI-PqxjmBrDc-cO5CBlP8dChYuXGo')

worksheet = sheet.get_worksheet(0)  # เลือก Worksheet ตาม index
data = worksheet.get_all_values()  # ดึงข้อมูลทั้งหมดในรูปแบบของ List

st.table(data)