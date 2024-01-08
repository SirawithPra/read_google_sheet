import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1q7I3Gw6wyEdsOxO1cMkVdFVT8Zq54CRNKNuhEtc2GdA/edit#gid=527336470"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)
df=pd.DataFrame(data)
df=df.dropna(how='all')
st.table(df)