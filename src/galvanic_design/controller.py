from galvanic_altium.project import AltiumProject


class Controller:
    def __init__(self, project_guid, name=None):
        self.project = AltiumProject(guid=project_guid)

        if name is None:
            name == self.project
        self.name = name

        print()