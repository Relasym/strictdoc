from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.reqif_objects.specobjectparser import SpecObjectParser
import pytest

pytest_plugins = [
    "test_mapping_fixtures.fixture_technical"
]


def test_mapping_technical_positive(fixture_technical_uid, fixture_technical_attribute_map,
                                    fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)

    # 3 assert
    # [LLR201]
    # [LLR204]
    assert (requirement.uid == "LLR204")
    # [/LLR204]
    # [LLR204]
    assert (
            requirement.title == "The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).")
    # [/LLR204]
    # [LLR204]
    assert (requirement.allocation_to_component == "Software")
    # [/LLR204]
    # [LLR204]
    assert (requirement.asil == "none")
    # [/LLR204]
    # [LLR204]
    assert (requirement.status == "Draft")
    # [/LLR204]
    # [LLR204]
    assert (requirement.target_value == "SPECIAL FIELD(initial_condition)")
    # [/LLR204]
    # [LLR204]
    assert (requirement.comment == "no comment")
    # [/LLR204]
    # [/LLR201]


def test_mapping_technical_uid_malformed(fixture_technical_uid_malformed, fixture_technical_attribute_map,
                                         fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid_malformed)
    # [LLR204]
    with pytest.raises(ValueError, match="uid_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_uid_missing(fixture_technical_uid_missing, fixture_technical_attribute_map,
                                       fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid_missing)
    # [LLR204]
    with pytest.raises(ValueError, match="uid_missing"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_allocation_to_component_malformed(fixture_technical_allocation_to_component_malformed,
                                                             fixture_technical_attribute_map,
                                                             fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_allocation_to_component_malformed)
    # [LLR204]
    with pytest.raises(ValueError, match="allocation_to_component_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_allocation_to_component_missing(fixture_technical_allocation_to_component_missing,
                                                           fixture_technical_attribute_map,
                                                           fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_allocation_to_component_missing)
    # [LLR204]
    with pytest.raises(ValueError, match="allocation_to_component_missing"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_asil_malformed(fixture_technical_asil_malformed, fixture_technical_attribute_map,
                                          fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_asil_malformed)
    # [LLR204]
    with pytest.raises(ValueError, match="asil_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_status_malformed(fixture_technical_status_malformed, fixture_technical_attribute_map,
                                            fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_status_malformed)
    # [LLR204]
    with pytest.raises(ValueError, match="status_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_target_value_malformed(fixture_technical_target_value_malformed,
                                                  fixture_technical_attribute_map, fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_target_value_malformed)
    # [LLR204]
    with pytest.raises(ValueError, match="target_value_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_target_value_missing(fixture_technical_target_value_missing, fixture_technical_attribute_map,
                                                fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_target_value_missing)
    # [LLR204]
    with pytest.raises(ValueError, match="target_value_missing"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_technical_description_malformed(fixture_technical_technical_description_malformed,
                                                           fixture_technical_attribute_map,
                                                           fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_technical_description_malformed)
    # [LLR204]
    with pytest.raises(ValueError, match="technical_description_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_technical_description_missing(fixture_technical_technical_description_missing,
                                                         fixture_technical_attribute_map,
                                                         fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_technical_description_missing)
    # [LLR204]
    with pytest.raises(ValueError, match="technical_description_missing"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]


def test_mapping_technical_comment_malformed(fixture_technical_comment_malformed, fixture_technical_attribute_map,
                                             fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_comment_malformed)
    # [LLR204]
    with pytest.raises(ValueError, match="comment_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR204]
