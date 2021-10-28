from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.reqif_objects.specobjectparser import SpecObjectParser
import pytest

pytest_plugins = [
    "test_mapping_fixtures.fixture_technical"
]

# [HLR101-T001]


def test_mapping_technical_uid_positive(fixture_technical_uid, fixture_technical_attribute_map,
                               fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)
    # 3 assert
    # [LLR104]
    assert (requirement.uid == "LLR104")
    # [/LLR104]


def test_mapping_technical_uid_malformed(fixture_technical_uid_malformed, fixture_technical_attribute_map,
                                         fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid_malformed)
    # [LLR104]
    with pytest.raises(ValueError, match="uid_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_uid_missing(fixture_technical_uid_missing, fixture_technical_attribute_map,
                                       fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid_missing)
    # [LLR104]
    with pytest.raises(ValueError, match="uid_missing"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_allocation_to_component_positive(fixture_technical_allocation_to_component,
                                                   fixture_technical_attribute_map,
                                                   fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_allocation_to_component)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)
    # 3 assert
    # [LLR104]
    assert (requirement.allocation_to_component == "Software")
    # [/LLR104]


def test_mapping_technical_allocation_to_component_malformed(fixture_technical_allocation_to_component_malformed,
                                                             fixture_technical_attribute_map,
                                                             fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_allocation_to_component_malformed)
    # [LLR104]
    with pytest.raises(ValueError, match="allocation_to_component_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_asil_positive(fixture_technical_asil, fixture_technical_attribute_map,
                                fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_asil)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)
    # 3 assert
    # [LLR104]
    assert (requirement.asil == "none")
    # [/LLR104]


def test_mapping_technical_asil_malformed(fixture_technical_asil_malformed, fixture_technical_attribute_map,
                                          fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_asil_malformed)
    # [LLR104]
    with pytest.raises(ValueError, match="asil_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_status_positive(fixture_technical_status, fixture_technical_attribute_map,
                                  fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_status)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)
    # 3 assert
    # [LLR104]
    assert (requirement.status == "Draft")
    # [/LLR104]


def test_mapping_technical_status_malformed(fixture_technical_status_malformed, fixture_technical_attribute_map,
                                            fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_status_malformed)
    # [LLR104]
    with pytest.raises(ValueError, match="status_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_target_value_positive(fixture_technical_target_value, fixture_technical_attribute_map,
                                        fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_target_value)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)
    # 3 assert
    # [LLR104]
    assert (requirement.target_value == "SPECIAL FIELD(initial_condition)")
    # [/LLR104]


def test_mapping_technical_target_value_malformed(fixture_technical_target_value_malformed,
                                                  fixture_technical_attribute_map, fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_target_value_malformed)
    # [LLR104]
    with pytest.raises(ValueError, match="target_value_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_target_value_missing(fixture_technical_target_value_missing, fixture_technical_attribute_map,
                                                fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_target_value_missing)
    # [LLR104]
    with pytest.raises(ValueError, match="target_value_missing"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_technical_description_positive(fixture_technical_technical_description,
                                                 fixture_technical_attribute_map,
                                                 fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_technical_description)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)
    # 3 assert
    # [LLR104]
    assert (
            requirement.title == "The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).")
    # [/LLR104]


def test_mapping_technical_technical_description_malformed(fixture_technical_technical_description_malformed,
                                                           fixture_technical_attribute_map,
                                                           fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_technical_description_malformed)
    # [LLR104]
    with pytest.raises(ValueError, match="technical_description_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_technical_description_missing(fixture_technical_technical_description_missing,
                                                         fixture_technical_attribute_map,
                                                         fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_technical_description_missing)
    # [LLR104]
    with pytest.raises(ValueError, match="technical_description_missing"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]


def test_mapping_technical_comment_positive(fixture_technical_comment, fixture_technical_attribute_map,
                                   fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_comment)

    # 2 test mapping
    requirement = SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map,
                                         fixture_technical_relation_map)
    # 3 assert
    # [LLR104]
    assert (requirement.comment == "no comment")
    # [/LLR104]


def test_mapping_technical_comment_malformed(fixture_technical_comment_malformed, fixture_technical_attribute_map,
                                             fixture_technical_relation_map):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_comment_malformed)
    # [LLR104]
    with pytest.raises(ValueError, match="comment_malformed"):
        SpecObjectParser.parse(xml_object, "test", fixture_technical_attribute_map, fixture_technical_relation_map)
    # [/LLR104]

# [/HLR101-T001]
