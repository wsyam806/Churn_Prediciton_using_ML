import streamlit as st
import pandas as pd 
import joblib
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf

page_bg_img = """
<style>[data-testid="stAppViewContainer"]{
background-color: #d1d1e6;
opacity: 0.2;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #d1d1e6 10px ), repeating-linear-gradient( #444cf755, #444cf7 );
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>


"""

Home, Dataset, App = st.tabs(['Home', 'Dataset', 'App'])

with Home:
  st.title("P2 Milestone 1 - Create a Robust Costumer Churn Prediction")
  st.subheader("Problem Statement")
  st.write('Create a robust costumer churn prediction to directly intialize and handle the appropriate actions to prevent costumers leaving our services')
  st.image('Customer-Churn.png')
  

with Dataset:
  st.title("Exploratory Data Analysis")
  dataset = st.container()
  
  with dataset:
    st.subheader("Dataset")
    st.write("The dataset is related to customer churn prediction, where the goal is to predict whether a customer is likely to churn based on the given features. Machine learning models can be trained on this dataset to predict the churn risk of customers, helping businesses take appropriate actions to retain customers and improve customer satisfaction.")
    df = pd.read_csv('churn.csv')
    st.dataframe(df)
    

with App:
  st.subheader("Churn Prediction")
  model_tf = tf.keras.models.load_model("model_best.hdf5")
  preprocess = joblib.load('full_pipeline.pkl')  
  
  df = pd.read_csv('churn.csv')
  df = preprocess.fit_transform(df)
  user_id = st.text_input('Your ID')  
  age = st.slider('age', 0,100)
  membership_category = st.selectbox('membership',['No Membership', 'Basic Membership','Silver Membership', 'Gold Membership', 'Premium Membership', 'Platinum Membership'])
  avg_transaction_value = st.slider('avg_transaction_value', 0,999999)
  avg_frequency_login_days = st.slider('avg_frequency_login_days', 0, 24)
  points_in_wallet = st.slider('points_in_wallet',0,9999999)
  feedback = st.selectbox('membership',['No reason specified', 'Poor Customer Service','Poor Product Quality', 'Poor Website', 'Products always in Stock', 'Quality Customer Care','Reasonable Price', 'Too many ads', 'User Friendly Website'])

  data = {
    'user_id': user_id,
    'age': age,
    'membership_category': membership_category,
    'avg_transaction_value': avg_transaction_value,
    'avg_frequency_login_days': avg_frequency_login_days,
    'points_in_wallet': points_in_wallet,
    'feedback': feedback,

  }
  input = pd.DataFrame(data, index=[0])
  st.subheader('User Input')
  st.write(input)
  if st.button('Predict'):
    process = preprocess.transform(input)
    prediction = model_tf.predict(process)
    if prediction == 1:
        prediction = 'Churn'
    else:
        prediction = 'Not Churn'

    st.write('Based on user input, the placement model predicted: ')
    st.write(prediction)
   
  