from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobjectparser import SpecObjectParser


def test_mapping_positive():
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

    # create test object
    test_object = SpecObjectParser(uid="SR001", status="Draft", allocation="Software", asil="none", functional_description="The import function shall import a .reqif file and convert it to an .sdoc file")

    # parse object here
    xml_object = etree.fromstring(object_string_pos, etree.XMLParser())

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object)

    # 3 assert
    assert (requirement.uid == test_object.uid)
    assert (requirement.status == test_object.status)
    assert (requirement.allocation == test_object.allocation)
    assert (requirement.asil == test_object.asil)
    assert (requirement.functional_description == test_object.functional_description)
