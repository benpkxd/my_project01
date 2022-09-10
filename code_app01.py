import streamlit as st
import pandas as pd
import numpy as np

st.title("🏠 Home")                                                                                              

st.header("👨‍🔬⚗️ Research Project 🔬")

# get data in to variable
df = pd.DataFrame({
'ID': [1,2,3,4],
'Project' : ['PCR 自配','PCR 鉴定','益生菌','养殖技术'],
'Type' : ['PCR','PCR','PRO','Other'],
'Rate' : [5,3,4,4]
})

st.write(df)

st.subheader("")


st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

 # make layout (sidebar)
st.sidebar.title("Working in Aqua Business")

 # For funny widget


option_1 = st.selectbox(
     'Which type you need to celebrate?',
     ('Balloon', 'snow'))

if option_1 == 'Balloon':
  st.balloons()
elif option_1 == 'snow':
  st.snow()
  

