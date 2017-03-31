import json

from tornado.httpclient import HTTPRequest, HTTPClient

from microservicesutils.settings import COMMENTS_API
from microservicesutils.logger import application

from frontend.services.user import get as get_user

def create(attributes):
    body = json.dumps(attributes)
    request = HTTPRequest(COMMENTS_API, 'POST', body=body)
    client = HTTPClient()

    try:
        response = client.fetch(request)
        json.loads(response.body.decode())
    except:
        application.error('error on create comment:' + str(e))
        return None

def get(resource_type, resource_uid):
    uri = "%s/%s/%s"%(COMMENTS_API, resource_type, resource_uid)
    client = HTTPClient()

    try:
        response = client.fetch(uri)
        comments = json.loads(response.body.decode())['data']['comments']
        for comment in comments:
            comment['user'] = get_user(comment['user'])
        return comments
    except Exception as e:
        application.error('error on recover comments:' + str(e))
        return []
