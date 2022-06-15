import json

class SettingsManager:

    appsettings: str = ""

    def __init__(self, settings):
        self.appsettings = settings


    def getAppsettings(self, key: str = "all"):
        with open(self.appsettings) as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()

        if(key == "all"):
            return jsonObject
        else:
            return jsonObject[key]

    def updateAppsettings(self, dictionary: dict):
        jsonObject = self.getAppsettings()
        for key in dictionary.keys():
            jsonObject[key] = dictionary[key]

        with open(self.appsettings, "w") as jsonOutFile:
            jsonOutFile.write(json.dumps(jsonObject))
            jsonOutFile.close()