from microservicesutils.resources import BaseResource

class Comment(BaseResource):

    def __init__(self, defaults = {}):
        self.init_attributes(['uid', 'user', 'resource_type', 'resource_uid', 'comment'],
            validations = {
                'user': {'required': True},
                'resource_type': {'required': True},
                'resource_uid': {'required': True},
                'comment': {'required': True}
            },
            defaults = defaults
        )

