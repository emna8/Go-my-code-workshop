from flask import Flask, jsonify,Response

app = Flask(__name__)


@app.route("/api/chatbot/basic/<string:sentence>")
def basic(sentence):
    return jsonify({"response":sentence})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

#train_model("entities.json") """