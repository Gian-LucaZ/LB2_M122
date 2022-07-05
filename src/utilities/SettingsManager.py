import json
from src.utilities import Logger


class SettingsManager:

    def __init__(self, settings):
        self.appsettings_loc = settings
        self.appsettings = None

    def proxy_get_appsettings(self, key: str = "all"):

        if self.appsettings is None:
            self.get_appsettings()

        if key == "all":
            return self.appsettings
        else:
            return self.appsettings[key]

    def get_appsettings(self):
        with open(self.appsettings_loc) as jsonFile:
            try:
                Logger.Information("Reading appsettings.")
                json_object: dict = json.load(jsonFile)
            except:
                Logger.Error("An error occurred while trying to read Appsettings.")
                exit(-1)

            jsonFile.close()

        self.appsettings = json_object

    def update_appsettings(self, dictionary: dict):
        json_object = self.proxy_get_appsettings()
        json_object_backup = dict(json_object)

        for key in dictionary.keys():
            json_object[key] = dictionary[key]

        Logger.Information("Now updating Appsettings.")

        with open(self.appsettings_loc, "w") as json_outFile:
            try:
                json_outFile.write(json.dumps(json_object, indent=4))
                Logger.Information("Successfully updated Appsettings")
            except:
                Logger.Error("Failed updating Appsettings.")
                Logger.Information("Trying to rollback now.")
                json_outFile.write(json.dumps(json_object_backup, indent=4))

            json_outFile.close()

    @staticmethod
    def to_dict(obj: object):
        return obj.__dict__
