import streamlit as st
import panda as pd
import numpy as np

st.title("🏠 Home")                                                                                              

st.header("👨‍🔬⚗️ Research Project 🔬")

                                                                                              # get data in to variable
df = pd.dataframe({
'ID': [1,2,3,4],
'Project' : ['PCR 自配','PCR 鉴定','益生菌','养殖技术']
'Type' : ['PCR','PCR','PRO','Other']
'Rate' : [5,3,4,4]
})

st.write(df)

st.subheader("")


st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

                                                                                              # make layout (sidebar)
st.sidebar.title("Working in Aqua Business")


                                                                                              # For funny widget
animate_1 = st.balloon()
animate_2 = st.snow()

option_1 = st.selectbox(
     'Which type you need to celebrate?',
     ('Balloon', 'snow'))

if option_1 == 'Balloon':
  animate_1
elif option_1 == 'snow':
  animate_2
  

