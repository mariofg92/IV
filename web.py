import os
from flask import Flask, Response, json, jsonfy
app = Flask(__name__)

@app.route("/")
def hello():
    '''response = app.response_class(
        response=json.dumps({"status": "OK"}),
        status=200,
        mimetype='application/json'
    )
    return response'''
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
