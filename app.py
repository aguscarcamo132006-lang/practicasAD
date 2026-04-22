
#
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/saludo", methods=["GET"])
def home():
    return jsonify({"mensaje": "API funcionando000000000"})


if __name__ == "__main__":
    app.run(debug=True)