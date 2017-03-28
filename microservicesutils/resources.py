import json

class BaseResource():

    def init_attributes(self, attributes, options = {}):
        self.attributes = {}
        for attribute in attributes:
            self.attributes[attribute] = ''

    def set_attribute(self, name, value):
        if not hasattr(self, 'attributes'):
            self.attributes = {}
        self.attributes[name] = value

    def get_attribute(self, name):
        if hasattr(self, 'attributes'):
            return self.attributes[name]

    def toJSON(self):
        return json.dumps(self.attributes)



