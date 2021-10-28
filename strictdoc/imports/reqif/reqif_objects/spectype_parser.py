import re
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element

import regex

# [HLR401]
class SpectypeParser:
    @staticmethod
    def parse(spectype):
        spectype_id = ""
        spectype_type = ""
        attribute_map = {}

        spectype: Element
        attributes = spectype.attrib
        try:
            spectype_id = attributes["IDENTIFIER"]
        except Exception:
            raise ValueError("id_missing")
        if len(spectype_id) < 1:
            raise ValueError("id_missing")
        regex_search = re.compile("^[a-zA-Z0-9_ ]+$")
        if not regex_search.match(spectype_id):
            raise ValueError("id_malformed")

        try:
            spectype_type = attributes["LONG-NAME"]
        except Exception:
            raise ValueError("type_missing")
        if len(spectype_type) < 1:
            raise ValueError("type_missing")
        if not regex_search.match(spectype_type):
            raise ValueError("malformed_type")
        if spectype_type not in {"functional", "FUNCTIONAL", "technical", "TECHNICAL", "test", "TEST"}:
            raise ValueError("unknown_type")

        spec_attributes = list(spectype)[0]
        for attribute_definition in spec_attributes:
            try:
                key = attribute_definition.attrib["LONG-NAME"]
                value = attribute_definition.attrib["IDENTIFIER"]
            except Exception:
                raise ValueError("attribute_malformed")
            attribute_map[key] = value

        return spectype_id, spectype_type, attribute_map
# [/HLR401]