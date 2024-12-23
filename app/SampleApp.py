import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    message = {
        "status": "success",
        "message": "Hello, this is a sample JSON response!",
        "data": {
            "app": "Sample Python App",
            "version": "1.0",
            "author": "Leonardo"
        }
    }
    return jsonify(message), 200

@app.route("/send", methods=["POST"])
def send_message():
    input_data = request.get_json()
    if not input_data:
        return jsonify({"error": "No JSON data received"}), 400

    response = {
        "status": "success",
        "received": input_data
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
