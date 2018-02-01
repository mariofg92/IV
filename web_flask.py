
from flask import Flask,request, jsonify
import os
import json

app = Flask(__name__)


@app.route("/")
def rutaStatus():
    return jsonify(status='OK')

@app.route("/status")
def rutaStatusDocker():
    return jsonify(status='OK')


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
