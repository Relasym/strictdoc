import time
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
            # requirement = Requirement()

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
            # initialize requirement object and assign values
            # requirement = Requirement()

        return Requirement("Type", "UID", "Content", "Status", 'status', 'tags', 'references', 'title', 'body',
                           'rationale', 'rationale_multiline', 'comments', 'special_fields')


# spec object type = test
object_attribute_map = {"_BSKKIS2GEeyvlO4vtsM_UA": "requirement_ID", "_BSKKJC2GEeyvlO4vtsM_UA": "type",
                        "_BSKKJS2GEeyvlO4vtsM_UA": "initial_condition", "_BSKKJi2GEeyvlO4vtsM_UA": "test_sequence",
                        "_a5wPYC2GEeyvlO4vtsM_UA": "target_value", "_DjbacC2MEeyvlO4vtsM_UA": "objective",
                        "_IjYFQC2XEeyvlO4vtsM_UA": "traceability", "_g_yJwC2XEeyvlO4vtsM_UA": "status"}

object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""

xml_object = etree.fromstring(object_string)


SpecObjectParser.parse(xml_object, "test", object_attribute_map)

