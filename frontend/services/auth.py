import json

from tornado.httpclient import HTTPRequest, HTTPClient

from microservicesutils.settings import USERS_AUTH_API

def is_valid_user(email, password):

    body = json.dumps({ "email": email, "password": password })

    request = HTTPRequest(USERS_AUTH_API, 'POST', body=body)

    client = HTTPClient()

    try:
        response = client.fetch(request)
        user = json.loads(response.body.decode())['data']['user']
        return user
    except:
        return None


