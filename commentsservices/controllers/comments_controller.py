from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

import json

from commentsservices.resources.comment import Comment
from commentsservices.models.comment import create_comment, list_comments
from commentsservices.models.comment import comments_as_resource, comment_as_resource

class ListCommentsController(APIHandler):

    def get(self, resource_type, resource_uid):
        comments = list_comments(resource_type, resource_uid)
        self.success({'comments': comments_as_resource(comments)})

class CommentsController(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "comment": {"type": "string"},
                "user": {"type": "string"},
                "resource_type": {"type": "string"},
                "resource_uid": {"type": "string"}
            }
        },
        input_example={
            "comment": "legal!",
            "user": "avaliduid",
            "resource_type": "book",
            "resource_uid": "avalidbookuid",
        },
        output_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "comment": {
                    "type": "object",
                    "properties": {
                        "comment": {"type": "string"},
                        "user": {"type": "string"},
                        "resource_type": {"type": "string"},
                        "resource_uid": {"type": "string"}
                    }
                }
            }
        },
        output_example={
            "message": "comment created",
            "comment": {
                "comment": "legal!",
                "user": "avaliduid",
                "resource_type": "book",
                "resource_uid": "avalidbookuid",
            }
        },
    )
    def post(self):
        comment = Comment(self.body)
        if comment.is_valid():
            uid = create_comment(comment.attributes)
            comment.set_attribute('uid', uid)
            self.set_status(201)
            return {
                'message': 'comment created',
                'comment': comment.attributes
            }
        else:
            self.set_status(422)
            return {
                'message': 'wrong comment',
                'comment': comment.attributes,
                'errors': comment.errors
            }

