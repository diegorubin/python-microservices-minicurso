import json

from tornado.httpclient import HTTPRequest, HTTPClient

from microservicesutils.settings import USERS_API
from microservicesutils.logger import application

def create(attributes):
    body = json.dumps(attributes)
    request = HTTPRequest(USERS_API, 'POST', body=body)
    client = HTTPClient()

    try:
        response = client.fetch(request)
        return json.loads(response.body.decode())['data']['user']
    except Exception as e:
        application.error('error on create user:' + str(e))
        return None

def index():
    client = HTTPClient()
    try:
        response = client.fetch(USERS_API)
        users = json.loads(response.body.decode())['data']['users']
        return users
    except Exception as e:
        application.error('error on recover users:' + str(e))
        return []

def get(uid):
    uri = "%s/%s"%(USERS_API, uid)
    client = HTTPClient()

    try:
        response = client.fetch(uri)
        attributes = json.loads(response.body.decode())['data']['user']
        return attributes
    except Exception as e:
        application.error('error on recover user:' + str(e))
        return None
