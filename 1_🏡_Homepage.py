import streamlit as st
import math
from collections import Counter
from sklearn.preprocessing import normalize
import numpy as np
from joblib import load
import matplotlib.pyplot as plt

model = load('random_forest_regressor_model.joblib')


def compute_tf(text):
    tf_text = Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i] / float(len(text))
    return tf_text


def compute_idf(word, corpus):
    return math.log10(len(corpus) / sum([1.0 for i in corpus if word in i]))


def tfidf_vectorize(text, n_features=200):
    # Creating a dynamic corpus
    corpus = [doc.split() for doc in text.split('.')]
    word_set = set()
    for doc in corpus:
        word_set = word_set.union(set(doc))

    tf = compute_tf(text.split())
    idfs = {word: compute_idf(word, corpus) for word in word_set}

    tfidf = np.zeros(len(word_set))
    for word in tf:
        if word in word_set:  # Check if word is in the word_set
            index = list(word_set).index(word)
            tfidf[index] = tf[word] * idfs[word]

    # Normalize and reshape
    tfidf_normalized = normalize(tfidf[:, np.newaxis], axis=0).ravel()

    # Adjust the length of the vector to n_features (200)
    if len(tfidf_normalized) < n_features:
        # Pad with zeros if the vector is shorter than 200
        padded_vector = np.pad(tfidf_normalized, (0, n_features - len(tfidf_normalized)), 'constant')
    else:
        # Truncate if the vector is longer than 200
        padded_vector = tfidf_normalized[:n_features]

    # Reshape to 2D array
    return padded_vector.reshape(1, -1)


st.set_page_config(
    page_title="Home Depo",
    page_icon="🏡",
)

st.title("Main Page - Home Depo")
st.sidebar.success("Select a page above.")

st.write(model)

if "search_term" not in st.session_state:
    st.session_state["search_term"] = ""

search_term = st.text_input("Search for a product",
                            st.session_state["search_term"])

submit = st.button("Submit")
if submit:
    st.session_state["search_term"] = search_term
    st.write("You have entered: ", search_term)

    prediction = model.predict(tfidf_vectorize(search_term))

    # Display the prediction
    st.write(f'Prediction: {prediction}')

    # Visualize the model's properties or predictions
    # For instance, plot feature importances for a tree-based model
    if hasattr(model, 'feature_importances_'):
        plt.bar(range(len(model.feature_importances_)),
                model.feature_importances_)
        st.pyplot(plt)
