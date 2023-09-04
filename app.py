import streamlit as st
import pandas as pd
import csv

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

csv_file_path = 'spam.csv'
df = pd.read_csv(csv_file_path)


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
    if input_upi in df['Phrases'].values:
        # Check if the corresponding 'v2' value is 1
        is_spam = df[df['Phrases'] == input_upi]['v2'].values[0] == 1
        if is_spam:
            st.header(f"Spam")
        else:
            st.header(f"Not Spam")
    else:
        st.header(f"Not Spam.")
else:
    st.write("Waiting for prediction...")
