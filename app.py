import streamlit as st
import pandas as pd
import joblib


st.title("Customer Churn Prediction App")
st.write("Use this app to predict whether a customer is likely to churn based on their age, tenure, and gender.")


data = pd.read_excel("churn_dataset.xlsx")
st.subheader("Dataset Review")
st.write(data.head())


data['Sex'] = data['Sex'].map({'Male': 1, 'Female': 0})
data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})


model = joblib.load("ccp.pkl")


st.sidebar.header("Enter Customer Details:")
age = st.sidebar.slider("Age", int(data['Age'].min()), int(data['Age'].max()), 35)
tenure = st.sidebar.slider("Tenure (months)", int(data['Tenure'].min()), int(data['Tenure'].max()), 10)
sex = st.sidebar.selectbox("Gender", ["Male", "Female"])


sex_value = 1 if sex == "Male" else 0


if st.sidebar.button("Predict Churn"):
    prediction = model.predict([[age, tenure, sex_value]])[0]
    result = "the customer will stay." if prediction == 0 else "the customer is likely to churn."
    st.subheader(result)
