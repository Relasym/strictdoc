import time
from xml.etree import ElementTree as etree

from strictdoc.backend.dsl.models.requirement import Requirement
from strictdoc.backend.dsl.models.special_field import SpecialField


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
    #       technical_description = {self.technical_description},
    #       functional_description = {self.functional_description})"""
    #
    #   def __repr__(self):
    #       return str(self)

    # def parse(element, element_type, attributes_map, relation_map):

    @staticmethod
    def parse(element, element_type, attribute_map):
        # check if value contains ' or "; if yes, raise an error; if no, append to list
        value_list = []
        for elem in element[0]:
            for char in elem:
                if char == '"' or char == "'" or char == "/":
                    raise ValueError("Attribute_contains_illegal_character")
            value_list.append(elem.attrib["THE-VALUE"])

        # append all identifiers from the spec object to an empty list
        identifier_list = []
        for identifier in element[0]:
            identifier_list.append(identifier[0][0].text)

        # check if all identifiers from attibute_map(from spec object type)
        # are in identifier_list(from spec object) and reversed
        # if not, raise ValueError;
        # ToDo make check of identifiers faster?
        identifier_counter = 0
        for identifier in identifier_list:
            for key in attribute_map:
                if identifier == key:
                    identifier_counter += 1
        if len(identifier_list) != identifier_counter or len(attribute_map) != identifier_counter:
            raise ValueError("SpecObject_identifiers_not_congruent")

        # dict with attribute names and corresponding identifiers
        value_number = 0
        dict_attribute_value = {}
        for identifier in identifier_list:
            dict_attribute_value[attribute_map[identifier]] = value_list[value_number]
            value_number += 1
        print(dict_attribute_value)
        # value_list        ['LLR001-T001', 'true'
        # identifier_list   ['_BSKKIS2GEeyvlO4vtsM_UA', '_a5wPYC2GEeyvlO4vtsM_UA',
        # attributes_map    {"_BSKKIS2GEeyvlO4vtsM_UA": "requirement_ID",
        #                   "_BSKKJC2GEeyvlO4vtsM_UA": "type",

        # check if values in attribute asil are correct asil values
        asil_values = ("ASIL A", "ASIL B", "ASIL C", "ASIL D",
                       "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D",
                       "A", "B", "C", "D", "QM")
        if element_type == "functional" or element_type == "technical":
            if dict_attribute_value["asil"] not in asil_values:
                raise ValueError("Attribute_asil_contains_no_asil_value")

        # check for missing attribute values in predefined spectypes
        if element_type == "test":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute != "type" and attribute != "status":
                        raise ValueError("Required_attribute_missing")
            # initialize requirement object and assign values
            requirement = Requirement(uid=dict_attribute_value["requirement_ID"], title=dict_attribute_value["title"],
                                      status=dict_attribute_value["status"], references=dict_attribute_value["traceability"],
                                      )

        if element_type == "technical":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute == "requirement_id" or attribute == "relation" or attribute == "technical_description":
                        raise ValueError("Required_attribute_missing")
            # initialize requirement object and assign values
            # requirement = Requirement()

        if element_type == "functional":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute == "requirement_id" or attribute == "functional_description":
                        raise ValueError("Required_attribute_missing")
            # initialize special fields
            """special_field_type = SpecialField(dict_attribute_value["requirement_ID"], "type",
                                              dict_attribute_value["type"])
            special_field_initial_condition = SpecialField(dict_attribute_value["requirement_ID"], "initial_condition",
                                                           dict_attribute_value["initial_condition"])
            special_field_test_sequence = SpecialField(dict_attribute_value["requirement_ID"], "test_sequence",
                                                       dict_attribute_value["test_sequence"])
            special_field_target_value = SpecialField(dict_attribute_value["requirement_ID"], "target_value",
                                                      dict_attribute_value["target_value"])"""
            # initialize requirement object and assign values
            requirement = Requirement(uid=dict_attribute_value["requirement_ID"],
                                      status=dict_attribute_value["status"])
            # requirement.requirement_from_dict(dict_attribute_value, dict_attribute_value["requirement_ID"])

        return Requirement("Type", "UID", "Content", "Status", 'status', 'tags', 'references', 'title', 'body',
                           'rationale', 'rationale_multiline', 'comments', 'special_fields')

