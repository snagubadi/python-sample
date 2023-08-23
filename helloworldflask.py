from flask import Flask

app = Flask(__name__)

@app.route('/hello1')
def helloIndex():
    return 'Hello Texas'

@app.route('/hello2')
def helloIndex1():
    return 'Hello California'
app.run(host='0.0.0.0', port=4444)