import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(worksheet='การตอบแบบฟอร์ม 1')
df=pd.DataFrame(data)
df=df.dropna(how='all')

    
#raw data
counts = pd.read_csv('number.txt', sep=",")
counts= pd.DataFrame(counts.T).reset_index()
counts.rename(columns={'index':'Class'
                    ,0:'All_Count'},inplace=True)
df=df.iloc[:,:7]

#EDA
df.rename(columns={'ประทับเวลา':'Time',
                   'ชื่อ สกุล':'Name',
                   'ชั้น':'Class',
                   'สังกัด':'BeUnder',
                   'จำหน่าย':'Participation',
                   'หมายเหตุ':'Etc',
                   'กรณีจำหน่ายมากกว่า 10 คนขึ้นไป':'Count'},inplace=True)
df.Class=df.Class.astype(int)
print(df.Count.value_counts())
df.loc[~(df.Count>0),'Count']=1
df
#all summary data
df2=df.groupby('Class').sum().reset_index()[['Class','Count']]
df3=pd.concat([counts,df2['Count']], axis=1, join="outer")
df3.loc[~(df3.Count>0),'Count']=0
df3=df3.set_index('Class')
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

data2 = conn.read(worksheet='การตอบแบบฟอร์ม 2')
dc=pd.DataFrame(data2)
dc=dc.dropna(how='all')
dc

submit=st.button(';;dsfsd')
if submit:
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(worksheet='การตอบแบบฟอร์ม 1')