
import pickle
from flask import Flask, request, jsonify

app = Flask("score")

# model2.bin is provided from svizor base image
model_file = "model2.bin"
vectorizer_file = "dv.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

with open(vectorizer_file, "rb") as f_in:
    dv = pickle.load(f_in)


def get_score(client):
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    return round(y_pred, 3)


@app.route("/score", methods=["POST"])
def score():
    client = request.get_json()
    score = get_score(client)
    result = {
        "credit_score": float(score),
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1234", debug=True)
