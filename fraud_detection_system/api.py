from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    return jsonify({
        "status": "API running",
        "records_received": len(df)
    })

if __name__ == "__main__":
    app.run(debug=True)
