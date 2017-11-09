from flask import Flask
import os
ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    new_port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    new_port = 5000

app = Flask(__name__)

@app.route('/')
def index():
   return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=new_port)
