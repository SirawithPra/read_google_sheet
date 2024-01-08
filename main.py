import os
import streamlit as st
import pandas as pd

output_filename = 'เช็คยอด.csv'
df = pd.DataFrame()
if os.path.isfile(output_filename):
	df = pd.read_csv(output_filename,index_col=False)
 
st.header("เช็คยอดคนจำหน่ายแถว")
st.write("การเช็คยอดรายวัน")

name = st.text_input( "ชื่อสกุล 👇",
                help='กรอกชื่อนามสกุลภาษาไทย อย่างครบถ้วน')
option2 = st.selectbox(
    'ชั้น',
    ('1', '2', '3','4','5'))
section = st.text_input( "สังกัด",
                help='ตัวอย่าง : 112')
option = st.selectbox(
    'จำหน่าย?',
    ('ราชการ', 'ลา', 'ป่วย','เสมียนเวรนักเรียน'))
dt = pd.Timestamp.now()

st.write("")
st.write("สรุป")
st.write("")
st.write('ชื่อ - สกุล : ', name)
st.write('ชั้น : ', option2)
st.write('สังกัด : ', section)
st.write('การจำหน่าย : ', option)
st.write('ประทับเวลา : ', dt)
genre = st.button('True')

if genre == True:
    new_row2 = {'ประทับเวลา': [dt], 'ชื่อ สกุล': [name],'ชั้น': [option2],'สังกัด': [section],'จำหน่าย':[option]}
    df2 = pd.DataFrame(new_row2)
    df3 =pd.concat([df[['ประทับเวลา','ชื่อ สกุล','ชั้น','สังกัด','จำหน่าย']],df2], axis=0)
    df3.to_csv(output_filename)
    st.write('บันทึกลงระบบเรียบร้อย')
    st.table(df2)