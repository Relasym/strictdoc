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
    def parse(specrelation):
        # ToDo: No definition of Target and Source!!
        """I can´t do anything!"""
        relation_map  = {}

# file = "../../../../tests/unit/strictdoc/import/reqif/mapping_testfile.reqif"


# https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
#
# file
#     spec-relations
#
#         spec-relation
#             source
#             target
#
# for invalid ID: Identifier contains "_ - . A-Z a-z 0-9"

