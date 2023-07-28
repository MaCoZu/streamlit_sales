import streamlit as st
import pandas as pd
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


def load_pickles(model_pickle_path):
    model_pickle_opener = open(model_pickle_path, "rb")
    model = pickle.load(model_pickle_opener)
    return model


def make_predictions(processed_df, model):
    prediction = model.predict(processed_df)
    return prediction


def generate_predictions(test_df):
    model_pickle_path = "./pipeline/lr_pipeline.pkl"

    model = load_pickles(model_pickle_path)

    record = competiton_distance, 
    prediction = make_predictions(processed_df, model)
    return prediction


if __name__ == '__main__':
    # make the application
    st.title("Stroe Sales Prediction")
    st.text("Enter store data")

    competiton_distance = st.slider("How far away is your competition in meters:", 0.0, 5000)
    competiton_distance = st.slider("How many customer do you expect in a day:", 0.0, 500)

    store_type = st.selectbox("Select the Store Type:", ('a', 'b', 'c', 'd'))

    # Assortment -  a = basic, b = extra, c = extended
    assortment = st.selectbox("Select the Assortment you plan to exhibit:", ("basic", "extra", "extended"))
    
    # generate the prediction for the customer
    if st.button("Predict Sales"):
        pred = generate_predictions(chosen_customer_data)
        if bool(pred):
            st.text("Customer will churn!")
        else:
            st.text("Customer not predicted to churn")
