class SpecObject:
    def __init__(self, object_type, object_uid, object_status, object_title, object_allocation, object_asil):
        self.object_type = object_type
        self.object_uid = object_uid
        self.object_title = object_title
        self.object_status = object_status
        self.object_allocation = object_allocation
        self.object_asil = object_asil

    def __str__(self):
        return f"SpecObject(object_type = {self.object_type}, object_uid = {self.object_uid}), object_content = {self.object_content}, object_status = {self.object_status})"

    def __repr__(self):
        return str(self)

    @staticmethod
    def parse(etree, attibutes_map):
        # actual parsing
        return SpecObject("Type", "UID", "Content", "Status")
