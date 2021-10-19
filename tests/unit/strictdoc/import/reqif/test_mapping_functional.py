from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobject import SpecObject
import pytest


@pytest.fixture
def fixture_functional():
    # spec_object_type = "functional"
    attributes_map = {
        "requirement_ID": "_FEHY0C2GEeyvlO4vtsM_UA",
        "functional_description": "_Hx6b0C2GEeyvlO4vtsM_UA",
        "allocation": "_KMVP0C2GEeyvlO4vtsM_UA",
        "asil": "_MZGCUC2GEeyvlO4vtsM_UA",
        "status": "_OlZh0C2GEeyvlO4vtsM_UA"
    }
    return attributes_map


def test_mapping_functional_positive(fixture_functional):
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:32:40.205+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SR001">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_FEHY0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_OlZh0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_KMVP0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""

    # parse object here
    xml_object = etree.fromstring(object_string_pos)

    # 2 test mapping
    spec_object = SpecObject.parse(xml_object, fixture_functional)

    # 3 assert
    # [LLR001-T001]
    assert (spec_object.uid == "SR001")
    # [/LLR001-T001]
    # [LLR005-T001]
    assert (spec_object.title == "The import function shall import a .reqif file and convert it to an .sdoc file")
    # [/LLR005-T001]
    # [LLR002-T001]
    assert (spec_object.allocation == "Software")
    # [/LLR002-T001]
    # [LLR003-T001]
    assert (spec_object.asil == "none")
    # [/LLR003-T001]
    # [LLR004-T001]
    assert (spec_object.status == "Draft")
    # [/LLR004-T001]
