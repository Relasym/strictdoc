from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobject import SpecObject


def test_mapping_test_positive():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="../reqif">
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
    xml_object = etree.fromstring(object_string_pos)

    # 2 test mapping
    spec_object = SpecObject.parse(xml_object, attributes_map)

    # 3 assert
    # [LLR201-T001]
    assert (spec_object.uid == "LLR001-T001")
    # [/LLR201-T001]
    # [LLR203-T001]
    assert (spec_object.type == "Software")
    # [/LLR203-T001]
    # [LLR204-T001]
    assert (spec_object.initial_condition == "ReqIF requirement_ID is passed into the mapping function.")
    # [/LLR204-T001]
    # [LLR208-T001]
    assert (spec_object.test_sequence == "The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.")
    # [/LLR208-T001]
    # [LLR207-T001]
    assert (spec_object.target_value == "true")
    # [/LLR207-T001]
    # [LLR206-T101]
    assert (spec_object.objective == "The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.")
    # [/LLR206-T101]
    # [LLR202-T001]
    assert (spec_object.traceability == r"tests\unit\strictdoc")
    # [/LLR202-T001]
    # [LLR205-T001]
    assert (spec_object.status == "Draft")
    # [/LLR205-T001]

