from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hellow_world():
    return 'Ola, estou na aplicação setada!'