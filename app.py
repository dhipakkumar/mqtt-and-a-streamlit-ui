import streamlit as st

# we have to get the input from the subscriber.py and display it real time on the streamlit app and also using the time.sleep() function so that it could be approximated as real time. maybe ....

# we should make sure that the publisher.py is running continuosly and the values we get are just the updated values and not the new pod creation values if you understand what i mean...

# implement a graphical view so that the engineer could understand how the pods are working
# in this use case i would be using plotly because its the best for interactive visualization


import plotly.express as px
import pandas as pd
data = "data.csv"
speed_data = [ ]
battery = [ ] 
with open(data,"r")as f:
    for i in f:
        i = eval(i)
        speed_data.append(i["speed"])
        battery.append(i["battery"])
col1,col2 = st.columns(2)
with col1:
    st.write("battery")
    st.bar_chart(speed_data)
with col2:
    st.write("speed")
    st.bar_chart(battery)
import time
time.sleep(2)
st.rerun()
