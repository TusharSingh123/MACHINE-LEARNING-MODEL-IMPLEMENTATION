import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def preprocess_text(message):
    # Convert to lowercase
    message = message.lower()
    tokens = nltk.word_tokenize(message)

    filtered_tokens = []
    for token in tokens:
        if token.isalnum():
            filtered_tokens.append(token)

    tokens = filtered_tokens[:]
    filtered_tokens.clear()

    for token in tokens:
        if token not in stopwords.words('english') and token not in string.punctuation:
            filtered_tokens.append(token)

    tokens = filtered_tokens[:]
    filtered_tokens.clear()

    for token in tokens:
        filtered_tokens.append(stemmer.stem(token))

    return " ".join(filtered_tokens)


# Load vectorizer and model
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
spam_classifier = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Email/SMS Spam Detector")

user_input = st.text_area("Type your message here")

if st.button("Predict"):
    # Step 1: Preprocess
    cleaned_message = preprocess_text(user_input)

    # Step 2: Vectorize
    input_vector = vectorizer.transform([cleaned_message])

    # Step 3: Prediction
    prediction = spam_classifier.predict(input_vector)[0]

    # Step 4: Output
    if prediction == 1:
        st.subheader("Spam")
    else:
        st.subheader("Not Spam")
