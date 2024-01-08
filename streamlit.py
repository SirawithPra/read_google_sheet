import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn = st.connection("gsheets", type=GSheetsConnection)
st.write('Test')
data = conn.read(worksheet='Test')
df=pd.DataFrame(data)
df=df.dropna(how='all')
df