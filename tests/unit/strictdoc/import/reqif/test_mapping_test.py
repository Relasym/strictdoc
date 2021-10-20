from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif.reqif_objects.specobjectparser import SpecObjectParser
import pytest

pytest_plugins = [
     "test_mapping_fixtures.fixture_test"
  ]


def test_mapping_test_positive(fixture_test_uid, fixture_test_attribute_map, fixture_test_relation_map):

    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_test_attribute_map, fixture_test_relation_map)

    # 3 assert
    # [LLR201-T001]
    assert (requirement.uid == "LLR001-T001")
    # [/LLR201-T001]
    # [LLR203-T001]
    assert (requirement.type == "Software")
    # [/LLR203-T001]
    # [LLR204-T001]
    assert (requirement.initial_condition == "ReqIF requirement_ID is passed into the mapping function.")
    # [/LLR204-T001]
    # [LLR208-T001]
    assert (requirement.test_sequence == "The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.")
    # [/LLR208-T001]
    # [LLR207-T001]
    assert (requirement.target_value == "true")
    # [/LLR207-T001]
    # [LLR206-T101]
    assert (requirement.objective == "The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.")
    # [/LLR206-T101]
    # [LLR202-T001]
    assert (requirement.traceability == r"tests\unit\strictdoc")
    # [/LLR202-T001]
    # [LLR205-T001]
    assert (requirement.status == "Draft")
    # [/LLR205-T001]


def test_mapping_test_uid_neg(fixture_test_uid_malformed, fixture_test_attribute_map, fixture_test_relation_map):

    # parse object here
    xml_object = etree.fromstring(fixture_test_uid_malformed)
    # [LLR201-T002]
    with pytest.raises(ValueError, match="uid_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_test_attribute_map, fixture_test_relation_map)
    # [/LLR201-T002]
