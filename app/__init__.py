from flask import Flask

app = Flask(__name__)

from app import routes

if __name__ == "main" :
    app.run(debug=True)
