# Todo: Implement ParserFunction
import re
from io import StringIO
from typing import List
from xml.etree import ElementTree as eTree
from xml.etree.ElementTree import Element
from strictdoc.imports.reqif import reqif


class SpecRelationParser:
    """currently no method"""

    @staticmethod
    def parse(input_element):
        # ToDo: No definition of Target and Source!!
        """I can´t do anything!"""
        with open(input_element, "r", encoding="UTF-8") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.read()
        try:
            parsed_xml = eTree.parse(StringIO(content), eTree.XMLParser())
        except Exception as e:
            assert 0

        parsed_spec_objects = []

        # https://stackoverflow.com/a/12946675/598057
        def get_namespace(element):
            m = re.match(r'\{.*\}', element.tag)
            return m.group(0) if m else ''

        top_level_reqif_element = parsed_xml.getroot()

        namespace = get_namespace(top_level_reqif_element)
        print(f"namespace: {namespace}")

        print(f"top level: {top_level_reqif_element}")

        top_level_reqif_element_children: List[Element] = list(top_level_reqif_element)
        core_content_element = top_level_reqif_element_children[1]
        print(f"CORE-CONTENT: {core_content_element}")

        core_content_element_children = list(core_content_element)
        reqif_content_element = core_content_element_children[0]
        print(f"REQ-IF-CONTENT: {reqif_content_element}")

        reqif_content_children = list(reqif_content_element)
        spec_objects = reqif_content_children[2]
        print(f"SPEC-OBJECTS: {spec_objects}")

        spec_objects_children = list(spec_objects)
        print(spec_objects_children[1])

# Todo: Filepath hardcoded!
# file = "../../../../tests/unit/strictdoc/import/reqif/mapping_testfile.reqif"

# SpecRelationParser.parse(file)

# https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
#
# file
#     spec-relations
#
#         spec-relation
#             source
#             target
#
# Identifier contains "_ - . A-Z a-z 0-9"

