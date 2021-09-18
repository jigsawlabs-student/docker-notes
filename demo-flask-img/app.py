from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'here we are'

app.run(host = '0.0.0.0', debug = True)
