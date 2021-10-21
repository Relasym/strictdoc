# Todo: Implement ParserFunction
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element

class SpecRelationParser:
    """currently no method"""

    @staticmethod
    def parse(element):
        # ToDo: No definition of Target and Source!!
        """I can´t do anything!"""
        with open(input_file, "r", encoding="UTF-8") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.read()
        try:
            parsed_xml = etree.parse(StringIO(content), etree.XMLParser())
        except Exception as e:
            assert 0