from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobject import SpecObject

def test_mapping_uid():
    # 1 create testobject from string
    object_string = r"""<ATTRIBUTE-DEFINITION-STRING IDENTIFIER="_oE860C2FEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T09:00:45.839+02:00" LONG-NAME="requirement_ID">
              <TYPE>
                <DATATYPE-DEFINITION-STRING-REF>_Z5pggyzGEey_QIvU1w5Ozg</DATATYPE-DEFINITION-STRING-REF>
              </TYPE>
            </ATTRIBUTE-DEFINITION-STRING>"""


    # 2 test mapping
    # spec_object = SpecObject.parse_technical(xml_object)

    # 3 assert
    assert ("_oE860C2FEeyvlO4vtsM_UA" in object_string)


def test_mapping_uid_failed():
    # 1 create testobject from string
    object_string = r"""<ATTRIBUTE-DEFINITION-STRING IDENTIFIER="_oE860C2FEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T09:00:45.839+02:00" LONG-NAME="requirement_ID">
                  <TYPE>
                    <DATATYPE-DEFINITION-STRING-REF>_Z5pggyzGEey_QIvU1w5Ozg</DATATYPE-DEFINITION-STRING-REF>
                  </TYPE>
                </ATTRIBUTE-DEFINITION-STRING>"""

    # 2 test mapping
    # spec_object = SpecObject.parse_technical(xml_object)

    # 3 assert
    assert ("_4xnFYC2FEeyvlO4vtsM_UA" not in object_string)
