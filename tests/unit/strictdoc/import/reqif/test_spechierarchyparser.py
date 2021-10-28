from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.reqif_objects.specrelationparser import SpecRelationParser
import pytest

spechierarchy_Object_string = r"""
    <SPECIFICATIONS>
        <SPECIFICATION IDENTIFIER="_Z5pgiizGEey_QIvU1w5Ozg" LAST-CHANGE="2021-10-14T10:11:59.495+02:00" LONG-NAME="Specification Document">
          <VALUES/>
          <TYPE>
            <SPECIFICATION-TYPE-REF>_Z5pghizGEey_QIvU1w5Ozg</SPECIFICATION-TYPE-REF>
          </TYPE>
          <CHILDREN>
            <SPEC-HIERARCHY IDENTIFIER="_eDzeoC2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T09:21:00.153+02:00">
              <OBJECT>
                <SPEC-OBJECT-REF>_eDO24C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
              </OBJECT>
              <CHILDREN>
                <SPEC-HIERARCHY IDENTIFIER="_lMO54C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T09:21:52.817+02:00">
                  <OBJECT>
                    <SPEC-OBJECT-REF>_lLoc8C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
                  </OBJECT>
                  <CHILDREN>
                    <SPEC-HIERARCHY IDENTIFIER="_sUCQwC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T09:58:25.954+02:00">
                      <OBJECT>
                        <SPEC-OBJECT-REF>_sTdpAC2NEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
                      </OBJECT>
                    </SPEC-HIERARCHY>
                    <SPEC-HIERARCHY IDENTIFIER="_IWY9oDDCEeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T11:51:21.674+02:00">
                      <OBJECT>
                        <SPEC-OBJECT-REF>_IV1kADDCEeyQ56CSv4ZenA</SPEC-OBJECT-REF>
                      </OBJECT>
                      <CHILDREN>
                        <SPEC-HIERARCHY IDENTIFIER="_M-4ywDDCEeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T11:51:57.013+02:00">
                          <OBJECT>
                            <SPEC-OBJECT-REF>_M-UyEDDCEeyQ56CSv4ZenA</SPEC-OBJECT-REF>
                          </OBJECT>
                          <CHILDREN/>
                        </SPEC-HIERARCHY>
                      </CHILDREN>
                    </SPEC-HIERARCHY>
                  </CHILDREN>
                </SPEC-HIERARCHY>
              </CHILDREN>
            </SPEC-HIERARCHY>
          </CHILDREN>
        </SPECIFICATION>
    </SPECIFICATIONS>"""
spechierarchy_Object = etree.fromstring(spechierarchy_Object_string)

spechierarchy_malformed_string = r"""
    <SPECIFICATIONS>
        <SPECIFICATION IDENTIFIER="_Z5pgiizGEey_QIvU1w5Ozg" LAST-CHANGE="2021-10-14T10:11:59.495+02:00" LONG-NAME="Specification Document">
          <VALUES/>
          <TYPE>
            <SPECIFICATION-TYPE-REF>_Z5pghizGEey_QIvU1w5Ozg</SPECIFICATION-TYPE-REF>
          </TYPE>
          <CHILDREN>
            <SPEC-HIERARCHY IDENTIFIER="_eDzeoC2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T09:21:00.153+02:00">
              <OBJECT>
                <SPEC-OBJECT-REF>_eDO24C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
              </OBJECT>
              <CHILDREN>
                <SPEC-HIERARCHY IDENTIFIER="_lMO54C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T09:21:52.817+02:00">
                  <OBJECT>
                    <SPEC-OBJECT-REF>_lLoc8C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
                  </OBJECT>
                  <CHILDREN>
                    <SPEC-HIERARCHY IDENTIFIER="_sUCQwC2N!Ee§yv§lO4vt%sM_UA" LAST-CHANGE="2021-10-15T09:58:25.954+02:00">
                      <OBJECT>
                        <SPEC-OBJECT-REF>_sTdpAC2NEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
                      </OBJECT>
                    </SPEC-HIERARCHY>
                    <SPEC-HIERARCHY IDENTIFIER="_IWY9o/DDC§EeyQ5"6CSv4ZenA" LAST-CHANGE="2021-10-19T11:51:21.674+02:00">
                      <OBJECT>
                        <SPEC-OBJECT-REF>_IV1kADDCEeyQ56CSv4ZenA</SPEC-OBJECT-REF>
                      </OBJECT>
                      <CHILDREN>
                        <SPEC-HIERARCHY IDENTIFIER="_M-4ywDDCEeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T11:51:57.013+02:00">
                          <OBJECT>
                            <SPEC-OBJECT-REF>_M-UyEDDCEeyQ56CSv4ZenA</SPEC-OBJECT-REF>
                          </OBJECT>
                          <CHILDREN/>
                        </SPEC-HIERARCHY>
                      </CHILDREN>
                    </SPEC-HIERARCHY>
                  </CHILDREN>
                </SPEC-HIERARCHY>
              </CHILDREN>
            </SPEC-HIERARCHY>
          </CHILDREN>
        </SPECIFICATION>
    </SPECIFICATIONS>"""
spechierarchy_malformed = etree.fromstring(spechierarchy_malformed_string)


# [LLR501-T001]
def test_spechierarchyparser_positive():
    hierarchy_map = SpecHierarchyParser.parse(spechierarchy_Object)

    assert (hierarchy_map["_M-UyEDDCEeyQ56CSv4ZenA"] == "_IV1kADDCEeyQ56CSv4ZenA")

# [/LLR501-T001]

def test_spechierarchyparser_invalidID():
    with pytest.raises(ValueError, match="spechierarchy_invalidID"):
        hierarchy_map = SpecHierarchyParser.parse(spechierarchy_malformed)


