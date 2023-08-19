import pickle
import numpy as np

from flask import Flask, request, jsonify

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

model_file = 'model_C=0.1.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    # gets the request json
    customer = request.get_json()

    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5
    
    result = {
        # we need to conver numpy data into python data in flask
        # therefore we convert them into float and bool
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    return jsonify(result)

# for production we may use WGSI server such as waitress
# (waitress-serve --listen=0.0.0.0:9696  "churn_service:app")
if __name__ == '__main__':
    # if run via gunicorn, this line won't be executed
    # app.run(debug=True, host='0.0.0.0', port=9696)
    serve(app, port=9696, host="0.0.0.0")