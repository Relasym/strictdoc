from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobject import SpecObject


def test_mapping_functional():
    # 1 create testobject from string
    object_string = """<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:32:40.205+02:00">
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

    # spec_object_type = "functional"
    attributes_map = {
        "requirement_ID": "_FEHY0C2GEeyvlO4vtsM_UA",
        "functional_description": "_Hx6b0C2GEeyvlO4vtsM_UA",
        "allocation": "_KMVP0C2GEeyvlO4vtsM_UA",
        "asil": "_MZGCUC2GEeyvlO4vtsM_UA",
        "status": "_OlZh0C2GEeyvlO4vtsM_UA"
    }

    # parse object here
    xml_object = etree.fromstring(object_string)

    # 2 test mapping
    spec_object = SpecObject.parse(xml_object, attributes_map)

    # 3 assert
    assert (spec_object.object_uid == "SR001")
    assert (spec_object.object_title == "The import function shall import a .reqif file and convert it to an .sdoc file")
    assert (spec_object.object_allocation == "Software")
    assert (spec_object.object_asil == "none")
    assert (spec_object.object_status == "Draft")
