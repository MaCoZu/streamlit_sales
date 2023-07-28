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
    st.title("Store Sales Prediction")
    st.subheader("Should you open a franchise")

    # customers = st.slider("How many customer do you expect in a day:", 100, 5000)

    st.markdown("<span style='font-size: 18px;'>How many customers do you expect in a day:</span>", unsafe_allow_html=True)
    customers = st.slider("", 100, 5000)

    st.markdown("<span style='font-size: 18px;'>How far away is your competition in meters:</span>", unsafe_allow_html=True)
    competiton_distance = st.slider("", 20, 2000)

    st.markdown("<span style='font-size: 18px;'>Since when is the competition there in month:</span>", unsafe_allow_html=True)
    competition_since = st.number_input("", min_value=1)
    
    col1, col2 = st.columns(2)

    # Store Type
    with col1:
        st.write("Select the Store Type:")
        store_type = st.radio("", options=['a', 'b', 'c', 'd'])

    # Assortment -  a = basic, b = extra, c = extended
    assortment_mapping = {"basic": "a", "extra": "b", "extended": "c"}
    with col2:
        st.write("Select the Assortment you plan to exhibit:")
        assortment = st.radio("", ("basic", "extra", "extended"))
        assort = assortment_mapping.get(assortment, "N/A")


    user_df = pd.DataFrame([{
                            'Customers':int(customers),
                            'CompetitionDistance':int(competiton_distance),
                            'Competition_Since_X_months':int(competition_since),
                            'StoreType':str(store_type),
                            'Assortment':str(assort)
                            }])
    
    st.text("")
    st.text("")
    st.text("")
    
    # generate the prediction for the customer
    if st.button("Predict Sales"):
        pred = generate_predictions(user_df)
        st.text(f"Expected Sales: {int(pred)}")

        if pred>7000:
            st.text("Open the Store")
        else:
            st.text("Open an Ice cream parlor")



    custom_css = """
    <style>
    /* Reduce the padding and margin of the elements */
    .element-container {
        padding: 0px;
        margin: 0px;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
