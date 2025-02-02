from flask import Flask, request, jsonify
from utils import model_predict
# from modify import preprocess
import pandas as pd
app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    email = data['content']
    text_series = pd.Series(email)
    # processed_text = preprocess(text_series)
    # email = preprocess(text_series)
    prediction = model_predict(email)
    return jsonify({'prediction': prediction, 'email': email})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
