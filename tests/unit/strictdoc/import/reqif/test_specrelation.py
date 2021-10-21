from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.reqif_objects.specobjectparser import SpecObjectParser
import pytest

pytest_plugins = [
    "test_mapping_fixtures.fixture_technical"
]

def spec_relation_object():
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



