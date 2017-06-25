import json
import logging
import requests
from steampill import config

logger = logging.getLogger(__name__)


class Steambot():
    """Represents the matrix-side bot that will be used for logging in and out from Steam.
    """

    def __init__(self):
        self.log_in(config.config['bot_username'],
                    config.config['bot_password'])

    def log_in(self, username, password):
        """Logs into the matrix server.
        """
        response = requests.post(
            config.config['server']
            + '/_matrix/client/r0/login',
            json.dumps({
                'type': 'm.login.password',
                'user': username,
                'password': password
            })
        )
        logger.info(response)
