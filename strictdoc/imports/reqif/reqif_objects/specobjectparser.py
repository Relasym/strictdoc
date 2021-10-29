from strictdoc.backend.dsl.models.requirement import Requirement
from strictdoc.backend.dsl.models.special_field import SpecialField


class SpecObjectParser:

    @staticmethod
    def parse(element, object_type_map, relation_map):

        # get type and attribute map

        element_type_identifier = element[1][0].text
        element_type = object_type_map[element_type_identifier][0]
        attribute_map = object_type_map[element_type_identifier][1]

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
        # ToDo make check of identifiers faster
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

        # check if values in attribute asil are correct asil values
        asil_values = ("ASIL A", "ASIL B", "ASIL C", "ASIL D",
                       "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D",
                       "A", "B", "C", "D", "QM", "")
        if element_type == "functional" or element_type == "technical":
            if dict_attribute_value["asil"] not in asil_values:
                raise ValueError("Attribute_asil_contains_no_asil_value")

        # get parents
        list_parents = relation_map[dict_attribute_value["requirement_ID"]]

        # check for missing attribute values in predefined spectypes
        if element_type == "test":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute != "type" and attribute != "status":
                        raise ValueError("Required_attribute_missing")
            # initialize special fields
            special_field_type = SpecialField(dict_attribute_value["requirement_ID"], "type",
                                              dict_attribute_value["type"])
            special_field_initial_condition = SpecialField(dict_attribute_value["requirement_ID"], "initial_condition",
                                                           dict_attribute_value["initial_condition"])
            special_field_test_sequence = SpecialField(dict_attribute_value["requirement_ID"], "test_sequence",
                                                       dict_attribute_value["test_sequence"])
            special_field_target_value = SpecialField(dict_attribute_value["requirement_ID"], "target_value",
                                                      dict_attribute_value["target_value"])
            special_fields = [special_field_type, special_field_initial_condition, special_field_test_sequence,
                              special_field_target_value]
            # return Requirement object
            return Requirement(list_parents, None, None, dict_attribute_value["requirement_ID"],
                               dict_attribute_value["status"], None, dict_attribute_value["traceability"],
                               dict_attribute_value["objective"], None, None, None, None, special_fields)

        if element_type == "technical":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute == "requirement_id" or attribute == "relation" or attribute == "technical_description":
                        raise ValueError("Required_attribute_missing")
            # initialize special fields
            special_field_asil = SpecialField(dict_attribute_value["requirement_ID"], "type",
                                              dict_attribute_value["asil"])
            special_field_allocation_to_component = SpecialField(dict_attribute_value["requirement_ID"],
                                                                 "allocation_to_component",
                                                                 dict_attribute_value["initial_condition"])
            special_field_target_value = SpecialField(dict_attribute_value["requirement_ID"],
                                                      "target_value",
                                                      dict_attribute_value["target_value"])
            special_fields = [special_field_asil, special_field_allocation_to_component,
                              special_field_target_value]
            # return Requirement object
            return Requirement(list_parents, None, None, dict_attribute_value["requirement_ID"],
                               dict_attribute_value["status"], None, None,
                               dict_attribute_value["technical_description"], None, None, None,
                               dict_attribute_value["comment"], special_fields)

        if element_type == "functional":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute == "requirement_id" or attribute == "functional_description":
                        raise ValueError("Required_attribute_missing")
            # initialize special fields
            special_field_asil = SpecialField(dict_attribute_value["requirement_ID"], "type",
                                              dict_attribute_value["asil"])
            special_field_allocation = SpecialField(dict_attribute_value["requirement_ID"], "allocation",
                                                    dict_attribute_value["initial_condition"])
            special_fields = [special_field_asil, special_field_allocation]
            # return Requirement object
            return Requirement(list_parents, None, None, dict_attribute_value["requirement_ID"],
                               dict_attribute_value["status"], None, None,
                               dict_attribute_value["functional_description"], None, None, None,
                               dict_attribute_value["comment"], special_fields)
