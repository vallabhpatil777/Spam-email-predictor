import streamlit as st
import pickle 
from nltk.corpus import stopwords
import nltk
import os
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')  # Use current working directory

if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

nltk.download('punkt_tab', download_dir=nltk_data_dir)

from nltk.stem.porter import PorterStemmer
nltk.download('stopwords',download_dir=nltk_data_dir)
nltk.data.path.append(nltk_data_dir)

import string 
ps = PorterStemmer()


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

def transform_text (text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    list = []
    for i in text:
        if i.isalnum():
            list.append(i)
    text = list[:]
    list.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            list.append(i)
    text = list[:]
    list.clear()
    for i in text:
        list.append(ps.stem(i))
    
    return " ".join(list)

st.title("Email/SMS Spam Predictor")

input_text = st.text_area("Enter Email/SMS : ")

if st.button("Predict"):

    processed_text = transform_text(input_text)
    vector_input = tfidf.transform([processed_text])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")

    else:
        st.header("Not Spam")