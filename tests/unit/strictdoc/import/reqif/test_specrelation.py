from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.reqif_objects.specrelationparser import SpecRelationParser
import pytest

specrelation_string_map = r"""      <SPEC-RELATIONS>
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
specrelation_map = etree.fromstring(specrelation_string_map)

specrelation_string_invalidID = r"""      <SPEC-RELATIONS>
        <SPEC-RELATION IDENTIFIER="_rFhEcDJJEeyeXuftE5Q6Cw" LAST-CHANGE="2021-10-21T10:34:11.458+02:00">
          <TARGET>
            <SPEC-OBJECT-REF>_l%Loc8C2IE?e:vlO4!vtsM_UA</SPEC-OBJECT-REF>
          </TARGET>
          <SOURCE>
            <SPEC-OBJECT-REF>_eD/O24C2IEe#yvlO4vtsäM_UA</SPEC-OBJECT-REF>
          </SOURCE>
          <TYPE>
            <SPEC-RELATION-TYPE-REF>_hD4AYDJJEeyeXuftE5Q6Cw</SPEC-RELATION-TYPE-REF>
          </TYPE>
        </SPEC-RELATION>
      </SPEC-RELATIONS>"""
specrelations_invalidID = etree.fromstring(specrelation_string_invalidID)

specrelation_string_missingID = r"""      <SPEC-RELATIONS>
        <SPEC-RELATION IDENTIFIER="_rFhEcDJJEeyeXuftE5Q6Cw" LAST-CHANGE="2021-10-21T10:34:11.458+02:00">
          <TARGET>
            <SPEC-OBJECT-REF></SPEC-OBJECT-REF>
          </TARGET>
          <SOURCE>
            <SPEC-OBJECT-REF></SPEC-OBJECT-REF>
          </SOURCE>
          <TYPE>
            <SPEC-RELATION-TYPE-REF>_hD4AYDJJEeyeXuftE5Q6Cw</SPEC-RELATION-TYPE-REF>
          </TYPE>
        </SPEC-RELATION>
      </SPEC-RELATIONS>"""
specrelations_missingID = etree.fromstring(specrelation_string_missingID)


# [LLR301-T001]
def test_specrelationparser_positive():
    assert (specrelation_map["_eDO24C2IEeyvlO4vtsM_UA"] == "_lLoc8C2IEeyvlO4vtsM_UA")


# [/LLR301-T001]


# [LLR301-T002]
def test_specrelationparser_malformed_invalidID():
    with pytest.raises(ValueError, match="specrelations_invalidID"):
        relation_map = SpecRelationParser.parse(specrelations_invalidID)


# [/LLR301-T002]

# [LLR301-T003]
def test_specrelationparser_malformed_missingID():
    with pytest.raises(ValueError, match="specrelations_missingID"):
        relation_map = SpecRelationParser.parse(specrelations_missingID)

# [/LLR301-T003]
