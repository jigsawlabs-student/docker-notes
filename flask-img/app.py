from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello everyone here world'

app.run(host = "0.0.0.0", debug = True)






