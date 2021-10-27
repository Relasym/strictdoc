from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.reqif_objects.specrelationparser import SpecRelationParser
import pytest


@pytest.fixture
def fixture_spec_relation_relation_object():
    # 1 create testobject from string
    object_string = r"""      <SPEC-RELATIONS>
        <SPEC-RELATION IDENTIFIER="_rFhEcDJJEeyeXuftE5Q6Cw" LAST-CHANGE="2021-10-21T10:34:11.458+02:00">
          <TARGET>
            <SPEC-OBJECT-REF>_lLoc8C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
          </TARGET>
          <SOURCE>
            <SPEC-OBJECT-REF>_eDO24C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
          </SOURCE>
          <TYPE>
            <SPEC-RELATION-TYPE-REF>_hD4AYDJJEeyeXuftE5Q6Cw</SPEC-RELATION-TYPE-REF>
          </TYPE>
        </SPEC-RELATION>
      </SPEC-RELATIONS>"""
    return object_string

@pytest.fixture
def fixture_spec_relation_relation_object_malformed():
    # 1 create testobject from string
    object_string = r"""      <SPEC-RELATIONS>
        <SPEC-RELATION IDENTIFIER="_rFhEcDJJEeyeXuftE5Q6Cw" LAST-CHANGE="2021-10-21T10:34:11.458+02:00">
          <TARGET>
            <SPEC-OBJECT-REF>_lLoc8C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
          </TARGET>
          <SOURCE>
            <SPEC-OBJECT-REF>_eDO24C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
          </SOURCE>
          <TYPE>
            <SPEC-RELATION-TYPE-REF>_hD4AYDJJEeyeXuftE5Q6Cw</SPEC-RELATION-TYPE-REF>
          </TYPE>
        </SPEC-RELATION>
      </SPEC-RELATIONS>"""
    return object_string


# [LLR301-T001]
def test_specrelationparser_positive(fixture_spec_relation_relation_object):
    xml_object = etree.fromstring(fixture_spec_relation_relation_object)
    relation_map = SpecRelationParser.parse(xml_object)

    assert (relation_map["_eDO24C2IEeyvlO4vtsM_UA"] == "_lLoc8C2IEeyvlO4vtsM_UA")
# [/LLR301-T001]


def test_specrelationparser_malformed_attribute(fixture_spec_relation_relation_object):



# Identifier contains "_ - . A-Z a-z 0-9"


#   < TARGET >
#   < SPEC - OBJECT - REF > _lLoc8C2IEeyvlO4vtsM_UA < / SPEC - OBJECT - REF >
#   < / TARGET >
#   < SOURCE >
#   < SPEC - OBJECT - REF > _eDO24C2IEeyvlO4vtsM_UA < / SPEC - OBJECT - REF >
#   < / SOURCE >
