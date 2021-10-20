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
    def parse(element):

        for elem in element[0]:
            print(elem.attrib)
        """for(attributes):
            get values;
            specobject.value = value
        check attributes;
        if technical attributes -> specobject.type = technical,
        if functional attr...;
        if other attr or attr missing -> parse_all
        """
        # raise ValueError("uid_malformed")
        return Requirement("Type", "UID", "Content", "Status",'status', 'tags', 'references', 'title', 'body', 'rationale', 'rationale_multiline', 'comments', 'special_fields')


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

SpecObjectParser.parse(xml_object)