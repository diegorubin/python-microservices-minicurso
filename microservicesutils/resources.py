class BaseResource():

    def init_attributes(self, attributes, options = {}):
        self.attributes = {}
        self.options = options

        if not 'defaults' in self.options:
            self.options['defaults'] = {}

        for attribute in attributes:
            if attribute in self.options['defaults']:
                self.attributes[attribute] = self.options['defaults'][attribute]
            else:
                self.attributes[attribute] = ''

    def set_attribute(self, name, value):
        if not hasattr(self, 'attributes'):
            self.attributes = {}
        self.attributes[name] = value

    def get_attribute(self, name):
        if hasattr(self, 'attributes'):
            return self.attributes[name]

    def is_valid(self):
        self.errors = {}
        for field, validations in self.options['validations'].items():
            for validation, args in validations.items():
                method = "check_%s_validation"%(validation)
                getattr(self, method)(field, args)

        return len(self.errors) == 0

    def check_required_validation(self, field, required):
        value = self.get_attribute(field)
        if required and (value is None or value == ''):
            if not field in self.errors:
                self.errors[field] = []
            self.errors[field].append('required')

