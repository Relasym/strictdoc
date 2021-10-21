from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.reqif_objects.spectype_parser import SpectypeParser

spectype_string = """<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="Requirement Type">
          <SPEC-ATTRIBUTES>
            <ATTRIBUTE-DEFINITION-STRING IDENTIFIER="_gFhrW2ojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="ReqIF.ForeignID">
              <TYPE>
                <DATATYPE-DEFINITION-STRING-REF>_gFhrVGojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
              </TYPE>
            </ATTRIBUTE-DEFINITION-STRING>
            <ATTRIBUTE-DEFINITION-STRING DESC="Testattribute" IDENTIFIER="_aqZG4GxpEeuaU7fHySy8Bw" LAST-CHANGE="2021-02-11T14:02:05.129+01:00" LONG-NAME="NOTES" IS-EDITABLE="true">
              <TYPE>
                <DATATYPE-DEFINITION-STRING-REF>_gFhrU2ojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
              </TYPE>
              <DEFAULT-VALUE/>
            </ATTRIBUTE-DEFINITION-STRING>
          </SPEC-ATTRIBUTES>
        </SPEC-OBJECT-TYPE>
"""
spectype = etree.fromstring(spectype_string)


def test_get_id():
    spectype_id, spectype_type, attribute_map = SpectypeParser.parse(spectype)
    assert (spectype_id == "_gFhrWmojEeuExICsU7Acmg")


def test_get_type():
    spectype_id, spectype_type, attribute_map = SpectypeParser.parse(spectype)
    assert (spectype_type == "Requirement Type")


def test_get_attribute_map():
    spectype_id, spectype_type, attribute_map = SpectypeParser.parse(spectype)
    assert (attribute_map.get("ReqIF.ForeignID") == "_gFhrXGojEeuExICsU7Acmg")
    assert (attribute_map.get("NOTES") == "_aqZG4GxpEeuaU7fHySy8Bw")
