from src import Requestor, Logger, PdfGenerator
from SettingsManager import SettingsManager

Logger.console_log("Starting Application", Logger.LogLevel.Information)

settings_manager = SettingsManager("Appsettings.json")

old_data = settings_manager.proxy_get_appsettings()
new_data = Requestor.get_api_data()

