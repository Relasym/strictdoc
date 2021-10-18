from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobject import SpecObject


def test_mapping_test():
    # 1 create testobject from string
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="tests\unit\strictdoc">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""

    # spec_object_type = "test"
    attributes_map = {
        "requirement_ID": "_BSKKIS2GEeyvlO4vtsM_UA",
        "type": "_BSKKJC2GEeyvlO4vtsM_UA",
        "initial_condition": "_BSKKJS2GEeyvlO4vtsM_UA",
        "test_sequence": "_BSKKJi2GEeyvlO4vtsM_UA",
        "target_value": "_a5wPYC2GEeyvlO4vtsM_UA",
        "objective": "_DjbacC2MEeyvlO4vtsM_UA",
        "reference": "_IjYFQC2XEeyvlO4vtsM_UA",
        "status": "_g_yJwC2XEeyvlO4vtsM_UA"
    }

    # parse object here
    xml_object = etree.fromstring(object_string)

    # 2 test mapping
    spec_object = SpecObject.parse(xml_object, attributes_map)

    # 3 assert
    assert (spec_object.uid == "LLR001-T001")
    assert (spec_object.type == "Software")
    assert (spec_object.initial_condition == "ReqIF requirement_ID is passed into the mapping function.")
    assert (spec_object.test_sequence == "The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.")
    assert (spec_object.target_value == "true")
    assert (spec_object.objective == "The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.")
    assert (spec_object.reference == r"tests\unit\strictdoc")
    assert (spec_object.status == "Draft")
