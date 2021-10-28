import re
from xml.etree.ElementTree import Element


class SpecHierarchyParser:

    @staticmethod
    def parse(spechierarchy):
        """Creates a Map of Child/Parent Links from an eTree Element,
        containing an SpecHierarchy ReqIF"""

        spechierarchy_list = list(spechierarchy)
        relation_map = {}
        relation_map: Element
        for hierarchy in spechierarchy_list:
            hierarchy: Element
            spechierarchy: Element

            # finds all Children from REQ-IF > CORE-Content > REQ-IF-CONTENT > SPECIFICATIONS > SPECIFICATION
            children_list = list(hierarchy)[2]
            relation_map.update(SpecHierarchyParser._getchild(children_list))

        return relation_map

    @staticmethod
    def _getchild(children_list):
        relation_map = {}
        if children_list != None:
            for hierarchy in children_list:
                spec_hierarchy: Element
                spec_hierarchy = list(hierarchy)
                object = spec_hierarchy[0]
                spec_object_ref = list(object)[0]
                value_id = spec_object_ref.text

                children = list(spec_hierarchy)[1]
                spec_hierarchy_children = children[0]
                object_children = spec_hierarchy_children[0]
                spec_object_ref = list(object_children)[0]
                key_id = spec_object_ref.text

                # Writes the key_id and value_id in the Dictionary relation_map
                relation_map[key_id] = value_id

                relation_map.update(SpecHierarchyParser._getchild(spec_hierarchy_children))
        return relation_map
