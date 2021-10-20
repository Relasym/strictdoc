# test_mapping_test.py
import pytest

@pytest.fixture
def fixture_test_attribute_map():
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
    return attributes_map

@pytest.fixture
def fixture_test_relation_map():
    # spec_object_type = "test"
    relation_map = {

    }
    return relation_map

@pytest.fixture
def fixture_test_uid():
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
    return object_string_pos

@pytest.fixture
def fixture_test_uid_malformed():
    # 1 create testobject from string
    object_string_neg = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="SR1114f'?">
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
    return object_string_neg

@pytest.fixture
def fixture_test_uid_missing():
    # 1 create testobject from string
    object_string_neg = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="">
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
    return object_string_neg

@pytest.fixture
def fixture_test_uid():
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
    return object_string_pos