import csv
import numpy as np
import pandas as pd 
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
# title
st.markdown('''
# **Exploratory Data Analysis web application**
This app is developed by Gulfam Mushtaq
 ''')

# how to upload file

with st.sidebar.header('Upload your dataset (.csv)'):
    uploaded_file = st.sidebar.file_uploader('Upload your file', type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown('[example csv file](df)')

# profile report

if uploaded_file is not None:
    @st.cache
    def load_csv():
        return csv

    df = load_csv()
    pr = ProfileReport(df, explorative= True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)

else:
    st.info('Awaiting for dataset')

    if st.button('Press to use example data'):
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),columns=['a','b','c','d','e'])
            return a

        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')

        st_profile_report(pr)



