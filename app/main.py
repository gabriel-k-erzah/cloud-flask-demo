from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify(message="Hello from Cloud Run! 🚀")


@app.get("healthz")
def health():
    return jsonify(status="ok")

@app.get("/info")
def info():
    return jsonify(
        service=os.environ.get("K_SERVICE"),
        version=os.environ.get("K_REVISION"),
        region=os.environ.get("K_REGION"),
    )

@app.errorhandler(404)
def page_not_found(e):
    """return jsonify(error=str(e)), 404 -> too verbose of a response potentially leaking internal details"""
    return jsonify(error="Not found"), 404