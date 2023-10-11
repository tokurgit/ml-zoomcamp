import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model_C1.0.bin'
app = Flask("churn")

# Open model_file and instruct that we will "rb" = Read Bytes
with open(model_file, "rb") as f_in:
    # Need also DictVectorizer, otherwise won't be able to translate a customer to feature matrix
    dv, model = pickle.load(f_in)

def predict_churn(customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5
    return y_pred, churn

@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()
    y_pred, churn = predict_churn(customer)

    result = {
        # Convert Numpy float64 to Python float
        "churn_probability": float(y_pred),
        # Convert Numpy boolean to Python boolean
        "churn": bool(churn),
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)