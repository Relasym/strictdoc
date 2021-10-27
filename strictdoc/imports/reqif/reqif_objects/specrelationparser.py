import re
from xml.etree.ElementTree import Element


class SpecRelationParser:

    @staticmethod
    def parse(specrelations):
        """Creates a Map of Child/Parent Links from an eTree Element,
        containing an SpecRelation ReqIF"""

        specrelation_list = list(specrelations)
        relation_map = {}
        for relation in specrelation_list:
            relation: Element
            specobjectref: Element
            children = list(relation)
            target = children[0]
            specobjectref = list(target)[0]
            value_ID = specobjectref.text

            source = children[1]
            specobjectref = list(source)[0]
            key_ID = specobjectref.text

            if value_ID == None:
                raise ValueError("specrelations_missingID")
            if key_ID == None:
                raise ValueError("specrelations_missingID")

            regex_search = re.compile("^[a-zA-Z0-9_\-.]+$")
            if not regex_search.match(key_ID):
                raise ValueError("specrelations_invalidID")
            if not regex_search.match(value_ID):
                raise ValueError("specrelations_invalidID")

            relation_map[key_ID] = value_ID
        return relation_map
