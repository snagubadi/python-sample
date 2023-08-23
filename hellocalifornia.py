from flask import Flask

app = Flask(__name__)


@app.route('/')
def hellocalifornia():
    return 'Hello California'
app.run(host='0.0.0.0', port=5555)