import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('XGBRegressor.pkl', 'rb'))
car = pd.read_csv('Cleaned_data.csv')

companies = car['company'].unique()
model_name = car['name'].unique()


def car_name(name):
    mod = []
    for company in companies:
        if selected_company == company:
            for m in model_name:
                if selected_company in m:
                    mod.append(m)
            return mod


def predict_str(prediction):
    for i in prediction:
        pred = str(i)
        return pred


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Car Price Prediction")

selected_company = st.selectbox("Select the company", sorted(car['company'].unique()))
act = car_name(selected_company)
selected_name = st.selectbox("Select the model", sorted(act))
selected_year = st.selectbox("Select the year of purchase", sorted(car['year'].unique(), reverse=True))
selected_fuel = st.radio("Select the fuel type", car['fuel_type'].unique(), horizontal=True)
selected_kms = st.number_input("How many kms driven", min_value=0, step=10)

if st.button("Predict"):
    predict = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                            data=np.array([selected_name, selected_company, selected_year, selected_kms,
                                                           selected_fuel]).reshape(1, 5)))
    prediction = predict_str(predict)
    st.text("This car can be sold for INR " + prediction)
