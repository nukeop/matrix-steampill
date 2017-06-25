from flask import Flask

app = Flask(__name__)

@app.route('/transactions/<transaction>', methods=['PUT'])
def on_event(transaction):
    pass
