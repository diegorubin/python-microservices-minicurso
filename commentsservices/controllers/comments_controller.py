from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

import json

from commentsservices.resources.comment import Comment
from commentsservices.models.comment import create_comment, list_comments
from commentsservices.models.comment import comments_as_resource, comment_as_resource

class ListCommentsController(APIHandler):

    def get(self, resource_type, resource_uid):
        pass

class CommentsController(APIHandler):

    def post(self):
        pass

