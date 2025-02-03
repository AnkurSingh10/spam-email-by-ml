import pickle

tf = pickle.load(open("model/tfidf_vectorizer.pkl", 'rb'))
model = pickle.load(open("model/model1.pkl", 'rb'))

def model_predict(email):
    if email == "":
        return ""
    tokenized_email = tf.transform([email]) # X 
    prediction = model.predict(tokenized_email)
    # If the email is spam, prediction should be 1
    prediction = 1 if prediction == 1 else -1
    return prediction
