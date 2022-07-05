import json
from src.utilities import Logger

appsettings_loc = "./config.json"
appsettings: dict = {}


def proxy_get_appsettings(key: str = "all"):
    if appsettings.__len__() == 0:
        get_appsettings()

    if key == "all":
        return appsettings
    else:
        return appsettings[key]


def get_appsettings():
    with open(appsettings_loc) as jsonFile:
        try:
            Logger.Information("Reading appsettings.")
            json_object: dict = json.load(jsonFile)
        except:
            Logger.Error("An error occurred while trying to read Appsettings.")
            exit(-1)

        jsonFile.close()

    appsettings.update(json_object)


def update_appsettings(dictionary: dict):
    json_object = proxy_get_appsettings()
    json_object_backup = dict(json_object)

    for key in dictionary.keys():
        json_object[key] = dictionary[key]

    Logger.Information("Now updating Appsettings.")

    with open(appsettings_loc, "w") as json_outFile:
        try:
            json_outFile.write(json.dumps(json_object, indent=4))
            Logger.Information("Successfully updated Appsettings")
        except:
            Logger.Error("Failed updating Appsettings.")
            Logger.Information("Trying to rollback now.")
            json_outFile.write(json.dumps(json_object_backup, indent=4))

        json_outFile.close()


def to_dict(obj: object):
    return obj.__dict__
