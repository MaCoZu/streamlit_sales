import streamlit as st
import pandas as pd
import pickle
import pandas as pd
import mypreprocess as p


def load_pickles(model_pickle_path):
    model_pickle_opener = open(model_pickle_path, "rb")
    model = pickle.load(model_pickle_opener)
    return model


def generate_predictions(df):
    model_pickle_path = "./pipeline/lr_pipeline.pkl"
    model = load_pickles(model_pickle_path)
    prediction = model.predict(df)
    return prediction


if __name__ == '__main__':
    # make the application
    st.title("Stroe Sales Prediction")
    st.text("Enter store data")

    customers = st.slider("How many customer do you expect in a day:", 100, 5000)
    competiton_distance = st.slider("How far away is your competition in meters:", 20, 2000)
    competition_since = st.number_input("Since when is the competition there in month:", min_value=1)

    store_type = st.radio("Select the Store Type:",  options=['a', 'b', 'c', 'd'])

    # Assortment -  a = basic, b = extra, c = extended
    assortment_mapping = { "basic": "a", "extra": "b", "extended": "c" }
    assortment = st.selectbox("Select the Assortment you plan to exhibit:", ("basic", "extra", "extended"))
    assort = assortment_mapping.get(assortment, "N/A")  

    user_df = pd.DataFrame([{
                            'Customers':int(customers),
                            'CompetitionDistance':int(competiton_distance),
                            'Competition_Since_X_months':int(competition_since),
                            'StoreType':str(store_type),
                            'Assortment':str(assort)
                            }])
    
    
    # generate the prediction for the customer
    if st.button("Predict Sales"):
        pred = generate_predictions(user_df)
        st.text(f"Expected Sales: {int(pred)}")

        if pred>7000:
            st.text("Open the Store")
        else:
            st.text("Open an Ice cream parlor")
