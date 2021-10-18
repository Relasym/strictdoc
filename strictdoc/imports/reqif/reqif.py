import re
from io import StringIO
from typing import List
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element

from strictdoc.backend.dsl.models.document import Document
from strictdoc.backend.dsl.models.document_config import DocumentConfig
from strictdoc.backend.dsl.models.section import Section
from strictdoc.backend.dsl.writer import SDWriter
from strictdoc.imports.reqif.reqif_objects.specobject import SpecObject


class Level:
    @staticmethod
    def parse_uid_as_int(int_str):
        pattern = re.compile("^[0-9]+$")
        if pattern.match(int_str):
            return int(int_str)
        return 0  # int_str TODO

    @staticmethod
    def compare(lhs, rhs):
        if len(lhs) < len(rhs):
            return 1
        elif len(lhs) > len(rhs):
            return -1
        else:
            return 0




class ReqIFImport:
    @staticmethod
    def import_from_file(input_file):
        with open(input_file, "r", encoding="UTF-8") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.read()
        try:
            parsed_xml = etree.parse(StringIO(content), etree.XMLParser())
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

        spec_object: Element
        for spec_object in spec_objects_children:
            object_type = None
            object_uid = None
            object_content = None

            spec_object_children = list(spec_object)
            print(spec_object_children)

            spec_object_values = spec_object_children[0]
            print(spec_object_values)

            spec_object_values_children = list(spec_object_values)

            spec_object_values_child: Element
            for spec_object_values_child in spec_object_values_children:
                # ElementTree -- provide a way to ignore namespace in tags and searches
                # https://bugs.python.org/issue18304
                if "ATTRIBUTE-VALUE-ENUMERATION" in spec_object_values_child.tag:
                    definition = spec_object_values_child.find(f"{namespace}DEFINITION")
                    string_ref = definition.find(f"{namespace}ATTRIBUTE-DEFINITION-ENUMERATION-REF");
                    value = string_ref.text
                    print(f"enum ref value: {value}")
                    if value == "_stype_requirement_kind":
                        attribute_values = (spec_object_values_child.find(f"{namespace}VALUES"))
                        enum_value_ref = (attribute_values.find(f"{namespace}ENUM-VALUE-REF"))
                        enum_value_ref_text = enum_value_ref.text
                        print(enum_value_ref_text)
                        object_type = enum_value_ref_text
                elif "ATTRIBUTE-VALUE-STRING" in spec_object_values_child.tag:
                    definition = spec_object_values_child.find(f"{namespace}DEFINITION")
                    string_ref = definition.find(f"{namespace}ATTRIBUTE-DEFINITION-STRING-REF");
                    value = string_ref.text
                    # print(value)
                    spec_object_title = (spec_object_values_child.get("THE-VALUE"))

                    if value == "_stype_requirement_requirementID":
                        # print(f"requirement ID: {spec_object_title}")
                        object_uid = spec_object_title
                    if value == "_stype_requirement_PlainText":
                        # print(f"requirement title: {spec_object_title}")
                        object_content = spec_object_title

            parsed_spec_objects.append(SpecObject(object_type, object_uid, object_content))

        document_config = DocumentConfig(None, "0.0.1", "DOC-N-001", [], None)
        document = Document("Test reqif", "Test reqif", document_config, [], [])

        current_section = document
        previous_level_components = [0]
        for parsed_spec_object in parsed_spec_objects[:20]:
            if (
                parsed_spec_object.object_type == "_enumVal_Kind_PLACEHOLDER" or
                parsed_spec_object.object_type == "_enumVal_Kind_TABLE" or
                parsed_spec_object.object_type == "_enumVal_Kind_FIGURE"
            ):
                continue

            print(parsed_spec_object)
            current_level_components = list(map(Level.parse_uid_as_int, parsed_spec_object.object_uid.split(".")))
            print(current_level_components)

            if parsed_spec_object.object_type == "_enumVal_Kind_HEADING":
                compare = Level.compare(previous_level_components, current_level_components)

                if compare == 1:
                    current_section = current_section.section_contents[-1]
                elif compare == -1:
                    current_section = current_section.parent
                else:
                    pass  # Intentionally nothing
                section = Section(
                    current_section, None, None, parsed_spec_object.object_content, [], []
                )
                section.ng_level = len(current_level_components)
                current_section.section_contents.append(section)

            previous_level_components = current_level_components

        document_content = SDWriter().write(document)
        with open("output/reqif.sdoc", 'w') as output_file:
            output_file.write(document_content)

