import streamlit as st
import seaborn as sns

st.header('My first dashboard')
st.text('yeah really first one')
st.header('BLAHHHHHHHH')

df = sns.load_dataset('iris')

st.write(df.head(10))

st.bar_chart(df['sepal_length'])

st.line_chart(df.sepal_length)

