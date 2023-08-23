from flask import Flask

app = Flask(__name__)

# this is for Texas
@app.route('/')
def hellotexas():
    return 'Hello Texas'

app.run(host='0.0.0.0', port=4444)