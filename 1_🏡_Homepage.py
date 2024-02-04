import streamlit as st
from joblib import load
import matplotlib.pyplot as plt

model = load('random_forest_regressor_model.joblib')

st.set_page_config(
    page_title="Home Depo",
    page_icon="🏡",
)

st.title("Main Page - Home Depo")
st.sidebar.success("Select a page above.")

st.write(model)

if "search_term" not in st.session_state:
    st.session_state["search_term"] = ""

search_term = st.text_input("Search for a product", st.session_state["search_term"])

submit = st.button("Submit")
if submit:
    st.session_state["search_term"] = search_term
    st.write("You have entered: ", search_term)
    
    prediction = model.predict(search_term)
    
    # Display the prediction
    st.write(f'Prediction: {prediction}')
    
    # Visualize the model's properties or predictions
    # For instance, plot feature importances for a tree-based model
    if hasattr(model, 'feature_importances_'):
        plt.bar(range(len(model.feature_importances_)), model.feature_importances_)
        st.pyplot(plt)
