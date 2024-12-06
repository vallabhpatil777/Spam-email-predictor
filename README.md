# Spam-email-predictor
A Machine Learning Web application built to predict whether an email or SMS is Spam or Not Spam using Natural Language Processing (NLP). The model analyzes text data and classifies it into spam and non-spam categories with high accuracy.

Key Features:

Real-time Spam Detection: Users can input any email or SMS text to predict if it is spam or not.
User-friendly Interface: Deployed as a web app using Streamlit, providing an easy-to-use interface for users.
High Accuracy: Achieved an accuracy of 98.5% and precision of 98% for spam detection.
Text Preprocessing & Feature Extraction: Used TF-IDF vectorization to convert text data into meaningful features for the machine learning model.
Model Evaluation: Multiple models were tested, with the final choice being the Multinomial Naive Bayes model for its superior performance.
Dataset:

The dataset used for training and evaluation was obtained from Kaggle and contains a total of 3,000 spam and non-spam emails/SMS messages. The dataset was preprocessed and cleaned for effective model training.

Model Training:

Text Preprocessing: Text data was preprocessed by removing stop words, punctuation, and converting the text to lowercase.
TF-IDF Vectorization: The text data was converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency), which is suitable for text classification tasks.
Model Selection: Several machine learning models were tested, and the Multinomial Naive Bayes model was chosen due to its excellent performance with text data.
Evaluation Metrics: The model achieved an accuracy of 98.5% and a precision of 98%, demonstrating high efficiency in classifying spam messages.
Technologies Used:

Streamlit: For building the frontend web application.
Python: The primary programming language used for the backend.
Numpy & Pandas: For data manipulation and preprocessing.
nltk: For text preprocessing and natural language processing tasks.
Scikit-learn: For implementing the machine learning model (Naive Bayes and TF-IDF vectorization).

Snapshots : 

![image](https://github.com/user-attachments/assets/d98ba981-9b0e-43e3-b61e-96669c4cef0c)



![image](https://github.com/user-attachments/assets/ad416233-c4dc-4953-862a-5e8c0628224e)
