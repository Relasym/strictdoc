from xml.etree import ElementTree as etree

from strictdoc.backend.dsl.models.requirement import Requirement


class SpecObjectParser:
    #   def __init__(self, test_type=None, uid=None, status=None, title=None, allocation=None,
    #                asil=None, objective=None, initial_condition=None, test_sequence=None, target_value=None,
    #                reference=None, allocation_to_component=None, comment=None, technical_description=None,
    #                functional_description=None):
    #       self.type = test_type
    #       self.uid = uid
    #       self.title = title
    #       self.status = status
    #       self.allocation = allocation
    #       self.asil = asil
    #       self.objective = objective
    #       self.initial_condition = initial_condition
    #       self.test_sequence = test_sequence
    #       self.target_value = target_value
    #       self.reference = reference
    #       self.allocation_to_component = allocation_to_component
    #       self.comment = comment
    #       self.technical_description = technical_description
    #       self.functional_description = functional_description
    #
    #   def __str__(self):
    #       """returns string"""
    #       return f"""SpecObject(type = {self.type}, uid = {self.uid}, title = {self.title}, status = {self.status},
    #       allocation = {self.allocation}, asil = {self.asil}, objective = {self.objective},
    #       initial_condition = {self.initial_condition}, test_sequence = {self.test_sequence},
    #       target_value = {self.target_value}, reference = {self.reference},
    #       allocation_to_component = {self.allocation_to_component}, comment = {self.comment},
    #       technical_description = {self.technical_description}, functional_description = {self.functional_description})"""
    #
    #   def __repr__(self):
    #       return str(self)

    # def parse(element, type, attributes_map, relation_map):

    @staticmethod
    def parse(element, attribute_map):
        # append all values to an empty list
        attribute_list = []
        for elem in element[0]:
            attribute_list.append(elem.attrib["THE-VALUE"])
        print(attribute_list)

        # append all identifiers from the spec object to an empty list
        identifier_list = []
        for identifier in element[0]:
            identifier_list.append(identifier[0][0].text)
        print(identifier_list)

        """check if all identifiers from attibute_map(from spec object type)
        are in identifier_list(from spec object) and reversed
        if not, raise ValueError"""
        identifier_counter = 0
        for identifier in identifier_list:
            for key in attribute_map:
                if identifier == key:
                    identifier_counter += 1

        if len(identifier_list) != identifier_counter or len(attribute_map) != identifier_counter:
            raise ValueError("SpecObjectIdentifiers not congruent")

        # print(identifier_list)

        # MISSING - dict with attribute names and corresponding identifiers
        """
        dict_attr = {}
        for identifier in identifier_list:
            for attribute in attribute_map:
                print(attribute_map.get(attribute))
        """
        # MISSING - check for missing or malformed (type : in technical relation required, in functional not
        # MISSING - initialize requirement object and assign values

        """for(attributes):
            get values;
            specobject.value = value
        check attributes;
        if technical attributes -> specobject.type = technical
        if functional attr...;
        if other attr or attr missing -> parse_all
        """
        # raise ValueError("uid_malformed")
        return Requirement("Type", "UID", "Content", "Status", 'status', 'tags', 'references', 'title', 'body',
                           'rationale', 'rationale_multiline', 'comments', 'special_fields')

