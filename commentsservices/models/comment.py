from peewee import CharField, TextField

from hashlib import sha256, md5

from microservicesutils.database import BaseModel
from commentsservices.resources.comment import Comment

class CommentModel(BaseModel):
    uid = CharField()
    user = CharField()
    resource_type = CharField()
    resource_uid = CharField()
    comment = TextField()

def comments_as_resource(models):
    return [comment_as_resource(model).attributes for model in models]

def comment_as_resource(model):
    resource = Comment()
    for attribute in resource.attributes:
        if hasattr(model, attribute):
            resource.set_attribute(attribute, getattr(model, attribute))
    return resource

def list_comments(resource_type, resource_uid):
    comments = (
        CommentModel.select()
        .where(CommentModel.resource_type == resource_type)
        .where(CommentModel.resource_uid == resource_uid)
    )
    return comments

def create_comment(attributes):
    uid_hash = sha256()
    uid_hash.update(attributes['comment'].encode('utf-8'))
    uid_hash.update(attributes['resource_type'].encode('utf-8'))
    uid_hash.update(attributes['resource_uid'].encode('utf-8'))

    comment = CommentModel.create(
        uid= uid_hash.hexdigest(),
        user=attributes['user'],
        resource_type=attributes['resource_type'],
        resource_uid=attributes['resource_uid'],
        comment=attributes['comment']
    )
    return comment.uid

