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

df=pd.DataFrame(data[1:],columns=data[0])
df.index += 1 
df[['ชื่อ สกุล','ชั้น','สังกัด', 'จำหน่าย', 'หมายเหตุ','กรณีจำหน่ายมากกว่า 10 คนขึ้นไป','ประทับเวลา']]
#EDA
df.rename(columns={'ประทับเวลา':'Time',
                   'ชื่อ สกุล':'Name',
                   'ชั้น':'Class',
                   'สังกัด':'BeUnder',
                   'จำหน่าย':'Participation',
                   'หมายเหตุ':'Etc',
                   'กรณีจำหน่ายมากกว่า 10 คนขึ้นไป':'Count'},inplace=True)
df.Class=df.Class.astype(int)
df.loc[df['Count']=='','Count']=1
df.Count=df.Count.astype(int)

#raw data
counts = pd.read_csv('number.txt', sep=",")
counts= pd.DataFrame(counts.T).reset_index()
counts.rename(columns={'index':'Class'
                    ,0:'All_Count'},inplace=True)

#all summary data
df2=df.groupby('Class').sum().reset_index()[['Class','Count']]
counts.Class=counts.Class.astype(int)
df2.Class=df2.Class.astype(int)
df3=pd.merge(counts, df2,how="left", on="Class")
df3.loc[~(df3.Count>0),'Count']=0
df3=df3.set_index('Class')
df3
sum = df3.sum()
sum.name = 'ยอดรวม'
sum
df3 = df3.append(sum.transpose())
st.write('')
st.header('ยอดรวม')
col1, col2, col3 = st.columns(3)
df3=df3.astype(int)
col1.table(df3)

dx=df.groupby('Participation').sum()['Count']
sum = pd.Series(dx.sum())
sum.name = 'ยอดรวม'
dx = dx.append(sum.transpose())
dx=dx.astype(int)
col2.table(dx)

for i in range(5):
    st.write('')
    st.header(f'ชั้น{i+1}')
    All_Count=df3.iloc[i]['All_Count']
    Count=df3.iloc[i]['Count']
    col1, col2, col3 = st.columns(3)
    col1.metric('ยอดเดิม',f'{All_Count}')
    col2.metric('จำหน่าย',f'{Count}')
    col3.metric('คงกอง',f'{All_Count-Count}')
    dx=df[df.Class==i+1].groupby('Participation').sum()['Count']
    dx

worksheet2 = sheet.get_worksheet(1)  # เลือก Worksheet ตาม index
data2 = worksheet2.get_all_values()  # ดึงข้อมูลทั้งหมดในรูปแบบของ List

dc=pd.DataFrame(data2[1:],columns=data2[0])
dc
