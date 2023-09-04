import streamlit as st
import pandas as pd
import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import csv

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


with open('vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf = pickle.load(vectorizer_file)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


def transformText(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum() and i not in stop_words:
            y.append(i)

    return ' '.join(y)



st.title("UPI Spam Classifier")

input_upi = st.text_input("Enter the ID.")
result = -1  # Default value

if st.button("Predict"):
    transformed_upi = transformText(input_upi)
    vector_input = tfidf.transform([transformed_upi])
    result = model.predict(vector_input)[0]


if result == 1:
    st.header("Spam")
elif result == 0:
    st.header("Not Spam")
else:
    st.write("Waiting for prediction...")