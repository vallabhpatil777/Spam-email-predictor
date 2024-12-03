import streamlit as st
import pickle 
from nltk.corpus import stopwords
import nltk
nltk.download('punkt_tab', download_dir='/Users/vallabhpatil777/Documents/ML-Projects/email-spam-detection/venv/nltk_data')

from nltk.stem.porter import PorterStemmer
nltk.download('stopwords',download_dir='/Users/vallabhpatil777/Documents/ML-Projects/email-spam-detection/venv/nltk_data')
nltk.data.path.append('/Users/vallabhpatil777/Documents/ML-Projects/email-spam-detection/venv/nltk_data')

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