import json


class SettingsManager:
    appsettings: str = ""

    def __init__(self, settings):
        self.appsettings = settings

    def get_appsettings(self, key: str = "all"):
        with open(self.appsettings) as jsonFile:
            json_object = json.load(jsonFile)
            jsonFile.close()

        if key == "all":
            return json_object
        else:
            return json_object[key]

    def update_appsettings(self, dictionary: dict):
        json_object = self.get_appsettings()
        for key in dictionary.keys():
            json_object[key] = dictionary[key]

        with open(self.appsettings, "w") as jsonOutFile:
            jsonOutFile.write(json.dumps(json_object, indent=4))
            jsonOutFile.close()

    @staticmethod
    def to_dict(obj: object):
        return obj.__dict__
