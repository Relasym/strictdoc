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
    def parse(element, type, attribute_map):
        # check if value contains ' or "; if yes, raise an error; if no, append to list
        value_list = []
        for elem in element[0]:
            for char in elem:
                if char == '"' or char == "'" or char == "/":
                    raise ValueError("Attribute_contains_illegal_character")
            value_list.append(elem.attrib["THE-VALUE"])
        print(value_list)

        # append all identifiers from the spec object to an empty list
        identifier_list = []
        for identifier in element[0]:
            identifier_list.append(identifier[0][0].text)
        print(identifier_list)

        # check if all identifiers from attibute_map(from spec object type)
        # are in identifier_list(from spec object) and reversed
        # if not, raise ValueError
        identifier_counter = 0
        for identifier in identifier_list:
            for key in attribute_map:
                if identifier == key:
                    identifier_counter += 1
        if len(identifier_list) != identifier_counter or len(attribute_map) != identifier_counter:
            raise ValueError("SpecObject_Identifiers_not_congruent")

        # dict with attribute names and corresponding identifiers
        value_number = 0
        dict_attribute_value = {}
        for identifier in identifier_list:
            for attribute in attribute_map:
                if identifier == attribute:
                    dict_attribute_value[attribute_map[attribute]] = value_list[value_number]
                    value_number += 1
        print(dict_attribute_value)

        # MISSING - check for missing
        # MISSING - initialize requirement object and assign values

        # UserWarning or ValueError??

        if type == "test":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute != "status":
                        raise UserWarning

        if type == "technical":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute == "status" or attribute == "relation" or attribute == "technical_description":
                        raise UserWarning
                    # if  format raise exc

        if type == "technical":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute == "status" or attribute == "technical_description":
                        raise UserWarning
                    # if  format raise exc

        """for(attributes):
            get values;
            specobject.value = value
        check attributes;
        if technical attributes -> specobject.type = technical
        if functional attr...;
        if other attr or attr missing -> parse_all
        """

        return Requirement("Type", "UID", "Content", "Status", 'status', 'tags', 'references', 'title', 'body',
                           'rationale', 'rationale_multiline', 'comments', 'special_fields')

