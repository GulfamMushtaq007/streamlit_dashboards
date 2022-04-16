import streamlit as st
import plotly.express as px
import pandas as pd


df = px.data.gapminder()
st.write(df)