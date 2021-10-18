class SpecObject:
    def __init__(self, type=None, uid=None, status=None, title=None, allocation=None,
                 asil=None, objective=None, initial_condition=None, test_sequence=None, target_value=None,
                 reference=None, allocation_to_component=None, comment=None, technical_description=None,
                 functional_description=None):
        self.type = type
        self.uid = uid
        self.title = title
        self.status = status
        self.allocation = allocation
        self.asil = asil
        self.objective = objective
        self.initial_condition = initial_condition
        self.test_sequence = test_sequence
        self.target_value = target_value
        self.reference = reference
        self.allocation_to_component = allocation_to_component
        self.comment = comment
        self.technical_description = technical_description
        self.functional_description = functional_description

    def __str__(self):
        """returns string"""
        return f"""SpecObject(type = {self.type}, uid = {self.uid}, title = {self.title}, status = {self.status},
        allocation = {self.allocation}, asil = {self.asil}, objective = {self.objective},
        initial_condition = {self.initial_condition}, test_sequence = {self.test_sequence},
        target_value = {self.target_value}, reference = {self.reference},
        allocation_to_component = {self.allocation_to_component}, comment = {self.comment},
        technical_description = {self.technical_description}, functional_description = {self.functional_description})"""

    def __repr__(self):
        return str(self)

    @staticmethod
    def parse(etree, attibutes_map):
        """actual parsing"""
        return SpecObject("Type", "UID", "Content", "Status")

    @staticmethod
    def parse_technical(etree, attibutes_map):
        """map only technical"""
        return SpecObject("Type", "UID", "Content", "Status")

    @staticmethod
    def parse_functional(etree, attibutes_map):
        """map only functional"""
        return SpecObject("Type", "UID", "Content", "Status")

    @staticmethod
    def parse_test(etree, attibutes_map):
        """map only test"""
        return SpecObject("Type", "UID", "Content", "Status")

