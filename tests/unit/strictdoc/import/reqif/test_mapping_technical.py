from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobjectparser import SpecObjectParser
import pytest


@pytest.fixture
def fixture_technical():
    # spec_object_type = "technical"
    attributes_map = {
        "requirement_ID": "_oE860C2FEeyvlO4vtsM_UA",
        "allocation_to_component": "_wgHwUC2FEeyvlO4vtsM_UA",
        "asil": "_4xnFYC2FEeyvlO4vtsM_UA",
        "status": "_-_ye4C2FEeyvlO4vtsM_UA",
        "target_value": "_7Eyo8C2FEeyvlO4vtsM_UA",
        "technical_description": "_rWmRwC2FEeyvlO4vtsM_UA",
        "comment": "_9J6iYC2FEeyvlO4vtsM_UA"
    }
    return attributes_map


def test_mapping_technical_positive(fixture_technical):
    # 1 create testobject from string
    object_string_pos = r"""</SPEC-OBJECT>
        <SPEC-OBJECT IDENTIFIER="_sTdpAC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:34:36.007+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="UID">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map requirement_ID to UID.">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""

    # parse object here
    xml_object = etree.fromstring(object_string_pos)

    # 2 test mapping
    requirement = SpecObjectParser.parse_technical(xml_object, fixture_technical)

    # 3 assert
    # []
    assert (requirement.uid == "LLR001")
    # [/]
    # []
    assert (requirement.title == "The mapping function shall map requirement_ID to UID.")
    # [/]
    # []
    assert (requirement.allocation_to_component == "Software")
    # [/]
    # []
    assert (requirement.asil == "none")
    # [/]
    # []
    assert (requirement.status == "Draft")
    # [/]
    # []
    assert (requirement.target_value == "UID")
    # [/]
    # []
    assert (requirement.comment == "no comment")
    # [/]
