import json

from tornado.httpclient import HTTPClient

from microservicesutils.settings import BOOKS_API
from microservicesutils.logger import application

def index():
    uri = "%s"%(BOOKS_API)
    client = HTTPClient()

    try:
        response = client.fetch(uri)
        books = json.loads(response.body.decode())['data']
        return books
    except Exception as e:
        application.error('error on recover books:' + str(e))
        return None

def get(isbn):
    uri = "%s/%s"%(BOOKS_API, isbn)
    client = HTTPClient()

    try:
        response = client.fetch(uri)
        attributes = json.loads(response.body.decode())['data']['book']
        return attributes
    except Exception as e:
        application.error('error on recover book:' + str(e))
        return None
