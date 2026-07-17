from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask Application",
        "status": "Application is Running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/about")
def about():
    return jsonify({
        "application": "Python Flask GHCR Demo",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)