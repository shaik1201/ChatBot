from flask import Flask, render_template, request, jsonify
import json
from chat import get_response

app = Flask(__name__)

@app.get("/")
def base():
    return render_template("base.html")


@app.post("/predict")
def predict():
    mes = request.get_data().decode("utf-8") 

    print(mes)
    if mes is None:
        return jsonify({'response': 'Invalid request. No message found.'})
    raw = get_response(mes)
    response = {'response': raw}
    return jsonify(response=response)


if __name__ == "__main__":
    app.run(debug=True)