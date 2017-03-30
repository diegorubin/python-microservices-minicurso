import unittest

from microservicesutils.resources import BaseResource

class A(BaseResource):
    def __init__(self, defaults = {}):
        self.init_attributes(['required_field'],
            validations = {
                'required_field': { 'required' : True }
            },
            defaults = defaults
        )

class TesResouces(unittest.TestCase):

    def test_required_validation(self):
        a = A()
        self.assertFalse(a.is_valid())

