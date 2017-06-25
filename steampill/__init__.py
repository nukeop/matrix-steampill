import logging
from flask import Flask, jsonify, request

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/transactions/<transaction>', methods=['PUT'])
def on_event(transaction):
    events = request.get_json()["events"]
    for event in events:
        logger.info("User: {} Room: {}".format(event["user_id"], event["room_id"]))
        logger.info("Event type: {}".format(event["type"]))
        logger.info("Content: {}".format(event["content"]))
    return jsonify({})
