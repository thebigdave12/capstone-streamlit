import streamlit as st;
import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt 

st.title('About the Data:')
st.markdown("***")
st.markdown('The data set used for this project comes from a fitness study that looked at 32 participants who actively wore Fitbit trackers over the course of a month. The participants came from a sample of mixed ages, fitness levels, and gender. Thus, it is representative of an active community of people who care about measuring and taking care of their health. For more details on the data set feel free to visit:')
st.markdown("https://www.kaggle.com/datasets/gloriarc/fitbit-fitness-tracker-data-capstone-project")
st.markdown("***")

st.markdown("<div style='text-align: center;'> <h2> By the Numbers </h2> </div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("Avg. Daily Step Count", "8,253")
col2.metric("Number of Participants", "32")
col3.metric("Total Daily Log (sample size)", "940")

st.markdown("***")

st.markdown("<div style='text-align: center;'> <h2> What was tracked in the study? </h2> </div>", unsafe_allow_html=True)
st.markdown("""
- Date of Log
- Daily Step Count
- Daily Distance by Mile
- Daily Total of Active minutes (very active, fairly active, lightly active)
- Daily Sedentary Minutes (time inactive)
- Daily Calories Burned
""")

            
st.markdown("<div style='text-align: center;'> <h2> Other things to note about Fitbit: </h2> </div>", unsafe_allow_html=True)

st.markdown("<div style='display: flex; justify-content: center;'>"
    "<img src='https://miro.medium.com/v2/resize:fit:1400/1*Rm5stTE51nPk7WxXhC6JDA.jpeg' style='height: 650px; display: block;'>"
    "</div>", unsafe_allow_html=True)


st.markdown("<div style='text-align: center;'> <h2> So what health metrics does Fitbit Track? </h2> </div>", unsafe_allow_html=True)
st.markdown("""
- Item 1
- Item 2
- Item 3
""")