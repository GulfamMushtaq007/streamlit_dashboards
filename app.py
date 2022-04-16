
import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


#make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Titanic Stats App")
    st.text('In this project we will work on tittanic data')

with data_sets:
    st.header('Titanic Wrecking')
    st.text('we will work with titanic dataset')

    #import data
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head())
    
    st.subheader('Sex: ')
    st.bar_chart(df['sex'].value_counts())

    st.subheader('Class:')
    st.bar_chart(df['class'].value_counts())

    st.bar_chart(df['age'].value_counts())

with features:
    st.header('These are our app features')
    st.text('Too many features')
    st.markdown('1. **Feature 1:** This will tell us about...')
    st.markdown('2. **Feature 2:** This will tell us about...')



with model_training:
    st.header('What happened to the people in titanic')
    st.text('We will chnage our parameters')

    #making columns
    input, display = st.columns(2)

    max_depth = input.slider('How many people do you know?', min_value=10, max_value=100, value=20, step=5)
   
# estimators
n_estimators = input.selectbox('How many trees?', options=[50,100,200,300,'No limit'])

# adding list of features
input.write(df.columns)


# input deatures
input_features = input.text_input('Feature')

#model

model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
if n_estimators == 'No limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

X = df[[input_features]]
y = df[['fare']]

model.fit(X,y)
pred = model.predict(y)

# Display 
display.subheader('Mean absolute error of the model is: ')
display.write(mean_absolute_error(y, pred))
display.subheader('Mean sq. error of the model is: ')
display.write(mean_squared_error(y, pred))
display.subheader('r2 score of the model is: ')
display.write(r2_score(y, pred))
