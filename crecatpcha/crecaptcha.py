"""
Codigos de errores:


100 - es humano
101 - fallo la comunicacion con google
102 - accion incorrecta
103 - no alcanzo el umbral esperadp

"""

import http.client, urllib.parse
import json
import logging

logger = logging.getLogger(__name__)

headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}


def request(payload):
    params = urllib.parse.urlencode(payload)
    conn = http.client.HTTPSConnection("www.google.com")
    conn.request('POST', '/recaptcha/api/siteverify', params, headers)
    return json.loads(conn.getresponse().read())


def is_a_human(secret_key, response_token, action=None, threshold=0.5):
    payload = {
        'secret': secret_key,
        'response': response_token
    }
    response = request(payload)
    if not response['success']:
        logger.warning("Failed comunication")
        return False, 101
    elif response["score"] >= threshold:
        if action and response.get('action', None):
            if action != response['action']:
                logger.warning("Bad action name. action send: %s , action expected: %s" % (action, response['action']))
                return False, 102
        logger.info("Is human")
        return True, 100
    else:
        logger.warning("Threshold failed, get: %s , expected < %s" % (response['score'], threshold))
        return False, 103


def crecaptcha(secret_key, response_token, action=None, threshold=0.5):
    ok, _ = is_a_human(secret_key, response_token, action, threshold)
    return ok
