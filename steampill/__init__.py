import json
import logging
import requests
from flask import Flask, jsonify, request

from .config import config
from .steambot.bot import Steambot

app = Flask(__name__)
logger = logging.getLogger(__name__)
steambot = Steambot()


@app.route('/transactions/<transaction>', methods=['PUT'])
def on_event(transaction):
    events = request.get_json()['events']
    for event in events:
        logger.info('User: {} Room: {}'.format(
            event['user_id'], event['room_id']))
        logger.info('Event type: {}'.format(event['type']))
        logger.info('Content: {}'.format(event['content']))
    return jsonify({})


@app.route('/rooms/<alias>')
def on_alias_query(alias):
    alias_localpart = alias.split(':')[0][1:]
    requests.post(
        config.config['server']
        + '/_matrix/client/api/v1/createRoom?access_token='
        + config.config['as_token'],
        json.dumps({
            'room_alias_name': alias_localpart
        }),
        headers = {'Content-Type': 'application/json'}
    )
    return jsonify({})
