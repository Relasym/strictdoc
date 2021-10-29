import re
from collections import defaultdict
from io import StringIO
from typing import List
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element

from strictdoc.backend.dsl.models.document import Document
from strictdoc.backend.dsl.models.document_config import DocumentConfig
from strictdoc.backend.dsl.models.section import Section
from strictdoc.backend.dsl.writer import SDWriter
from strictdoc.imports.reqif.reqif_objects.spectype_parser import SpectypeParser
from strictdoc.imports.reqif.reqif_objects.specrelationparser import SpecRelationParser

# TODO uncomment this and the relevant code below once SpecHierarchyParser is implemented
# from strictdoc.imports.reqif.reqif_objects.specrhierarchyparser import SpecHierarchyParser

from strictdoc.imports.reqif.reqif_objects.specobjectparser import SpecObjectParser


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
        # TODO things missing:
        # - datatypes
        # - output path
        # - SDoc Sections (currently the multiple specifications are shown together)
        # - Sections

        # import file
        with open(input_file, "r", encoding="UTF-8") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.read()
        try:
            parsed_xml = etree.parse(StringIO(content), etree.XMLParser())
        except Exception as e:
            # TODO handle
            pass

        # reqif element naming convention: element_xyz where xyz is the name of the reqif(xml) tag.
        # dashes are turned into underscores
        element_req_if = parsed_xml.getroot()

        # need to get the namespace for all finds, etc
        # https://stackoverflow.com/a/12946675/598057
        def get_namespace(element):
            m = re.match(r'\{.*\}', element.tag)
            return m.group(0) if m else ''

        namespace = get_namespace(element_req_if)
        # also create a dictionary of namespaces for Element.find() (slice removes curly braces)
        namespace_dict = {"": namespace[1:-1]}

        # getting all structural elements from the reqif tree:

        # the header, containg metadata about the document
        element_the_header = element_req_if.find("THE-HEADER",namespace_dict)

        # core content, contains req-if-content which contains all the actual content
        element_core_content = element_req_if.find("CORE-CONTENT", namespace_dict)

        # tool extensions contains information specific to the tool used to create the reqif
        element_tool_extensions = element_req_if.find("TOOL-EXTENSIONS", namespace_dict)

        # req-if-content contains the requirements and structure
        element_req_if_content = element_core_content.find("REQ-IF-CONTENT", namespace_dict)

        # datatypes contains the various datatypes used to store information
        element_datatypes = element_req_if_content.find("DATATYPES", namespace_dict)

        # spec-types contains the spectypes, basically blueprints for specobjects.
        # spec-types use datatypes to define the kind of information stored
        element_spec_types = element_req_if_content.find("SPEC-TYPES", namespace_dict)

        # spec-objects contains specobjects, which are the actual requirements.
        # every specobject must have a spectype which defines its structure
        element_spec_objects = element_req_if_content.find("SPEC-OBJECTS", namespace_dict)

        # spec-relations contains arbitrarily defined relations between specobjects.
        # these relations may be grouped into relationgroups which have user-defined meaning
        element_spec_relations = element_req_if_content.find("SPEC-RELATIONS", namespace_dict)

        # specifications contains one or more specification elements. each specification element contains
        # a tree of spec-hierarchy elements which represents the basic structure of the document
        # each spec-hierarchy element contains a spec-object
        element_specifications = element_req_if_content.find("SPECIFICATIONS", namespace_dict)

        # Note: the other objects have to be present in a proper ReqIF file as well,
        # but these two are absolutely required
        if element_spec_types is None or element_spec_objects is None:
            raise ValueError("invalid ReqIF structure")

        # parse spectypes, create a map storing relevant data for each spectype
        parsed_spectypes = {}
        for spectype in list(element_spec_types):
            type_id, type_name, type_map = SpectypeParser.parse(spectype)
            type_data = {type_name, type_map}
            parsed_spectypes[type_id] = type_data

        # get links between requirements:
        structure_map = defaultdict(list)
        # TODO uncomment this and the import statement once SpecHierarchyParser is implemented
        # if element_specifications is not None:
        #     hierarchy_map = SpecHierarchyParser.parse(element_specifications)
        #     for k, v in hierarchy_map:
        #         structure_map[k].append(v)
        if element_spec_relations is not None:
            relation_map = SpecRelationParser.parse(element_spec_relations)
            for k, v in relation_map:
                structure_map[k].append(v)

        # with parsed spectypes and structure map, parse each specobject into a SDoc requirement
        requirements = []
        for spec_object in element_spec_objects:
            requirement = SpecObjectParser.parse(spec_object, parsed_spectypes, structure_map)
            requirements.append(requirement)

        # spec_object: Element
        # for spec_object in element_spec_objects:
        #     object_type = None
        #     object_uid = None
        #     object_content = None
        #
        #     spec_object_children = list(spec_object)
        #     print(spec_object_children)
        #
        #     spec_object_values = spec_object_children[0]
        #     print(spec_object_values)
        #
        #     spec_object_values_children = list(spec_object_values)
        #
        #     spec_object_values_child: Element
        #     for spec_object_values_child in spec_object_values_children:
        #         # ElementTree -- provide a way to ignore namespace in tags and searches
        #         # https://bugs.python.org/issue18304
        #         if "ATTRIBUTE-VALUE-ENUMERATION" in spec_object_values_child.tag:
        #             definition = spec_object_values_child.find(f"{namespace}DEFINITION")
        #             string_ref = definition.find(f"{namespace}ATTRIBUTE-DEFINITION-ENUMERATION-REF");
        #             value = string_ref.text
        #             print(f"enum ref value: {value}")
        #             if value == "_stype_requirement_kind":
        #                 attribute_values = (spec_object_values_child.find(f"{namespace}VALUES"))
        #                 enum_value_ref = (attribute_values.find(f"{namespace}ENUM-VALUE-REF"))
        #                 enum_value_ref_text = enum_value_ref.text
        #                 print(enum_value_ref_text)
        #                 object_type = enum_value_ref_text
        #         elif "ATTRIBUTE-VALUE-STRING" in spec_object_values_child.tag:
        #             definition = spec_object_values_child.find(f"{namespace}DEFINITION")
        #             string_ref = definition.find(f"{namespace}ATTRIBUTE-DEFINITION-STRING-REF");
        #             value = string_ref.text
        #             # print(value)
        #             spec_object_title = (spec_object_values_child.get("THE-VALUE"))
        #
        #             if value == "_stype_requirement_requirementID":
        #                 # print(f"requirement ID: {spec_object_title}")
        #                 object_uid = spec_object_title
        #             if value == "_stype_requirement_PlainText":
        #                 # print(f"requirement title: {spec_object_title}")
        #                 object_content = spec_object_title
        #
        #     parsed_spec_objects.append(SpecObject(object_type, object_uid, object_content))

        document_config = DocumentConfig(None, "0.0.1", "DOC-N-001", [], None)
        document = Document("Test reqif", "Test reqif", document_config, [], [])

        # current_section = document
        # previous_level_components = [0]
        # for parsed_spec_object in parsed_spec_objects[:20]:
        #     if (
        #             parsed_spec_object.object_type == "_enumVal_Kind_PLACEHOLDER" or
        #             parsed_spec_object.object_type == "_enumVal_Kind_TABLE" or
        #             parsed_spec_object.object_type == "_enumVal_Kind_FIGURE"
        #     ):
        #         continue
        #
        #     print(parsed_spec_object)
        #     current_level_components = list(map(Level.parse_uid_as_int, parsed_spec_object.object_uid.split(".")))
        #     print(current_level_components)
        #
        #     if parsed_spec_object.object_type == "_enumVal_Kind_HEADING":
        #         compare = Level.compare(previous_level_components, current_level_components)
        #
        #         if compare == 1:
        #             current_section = current_section.section_contents[-1]
        #         elif compare == -1:
        #             current_section = current_section.parent
        #         else:
        #             pass  # Intentionally nothing
        #         section = Section(
        #             current_section, None, None, parsed_spec_object.object_content, [], []
        #         )
        #         section.ng_level = len(current_level_components)
        #         current_section.section_contents.append(section)
        #
        #     previous_level_components = current_level_components

        # TODO fix dummy path
        document_content = SDWriter().write(document)
        with open("output/reqif.sdoc", 'w') as output_file:
            output_file.write(document_content)
