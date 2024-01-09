import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


conn = st.connection("gsheets", type=GSheetsConnection)
st.write('Test')
data = conn.read(worksheet='การตอบแบบฟอร์ม 1')
df=pd.DataFrame(data)
# df=df.dropna(how='all')
df2=df.groupby(['ชั้น']).count()


#result
df
df2
st.bar_chart(df2['ประทับเวลา'])
fig = px.scatter(df, x="ชั้น", y="สังกัด [พัน.]",title= "test", template="plotly_dark")
fig
fig = px.pie(df, names='ชั้น')
fig
df3=df2=df.groupby(['อื่นๆ รายละเอียด']).count()
df3.rename(columns={'ชื่อ สกุล':'จำนวนคน'},inplace=True)
df3['จำนวนคน']
df.shape