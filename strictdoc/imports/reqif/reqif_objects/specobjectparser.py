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
            raise ValueError("SpecObject_Identifiers_not_congruent")




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


object_attribute_map = {"_BSKKIS2GEeyvlO4vtsM_UA": "requirement_ID", "_BSKKJC2GEeyvlO4vtsM_UA": "type",
                        "_BSKKJS2GEeyvlO4vtsM_UA": "initial_condition", "_BSKKJi2GEeyvlO4vtsM_UA": "test_sequence",
                        "_a5wPYC2GEeyvlO4vtsM_UA": "target_value", "_DjbacC2MEeyvlO4vtsM_UA": "objective",
                        "_IjYFQC2XEeyvlO4vtsM_UA": "traceability", "_g_yJwC2XEeyvlO4vtsM_UA": "status"}

specobject = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:50:26.322+02:00">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDOC attribute UID.">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed into the function and the function returns the same value as result and compares it to the predefined test value.">
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

xml_object = etree.fromstring(specobject)

SpecObjectParser.parse(xml_object, object_attribute_map)
