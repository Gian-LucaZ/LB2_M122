from src import Requestor
from SettingsManager import SettingsManager

sm = SettingsManager("config.json")

Requestor.get_access_token(sm.proxy_get_appsettings()["apis"]["tokenApi"])