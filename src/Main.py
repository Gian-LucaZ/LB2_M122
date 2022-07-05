from src.utilities import Requestor, Logger
from src.utilities.PdfGenerator import Generator
from src.utilities.SettingsManager import SettingsManager
from src.typedefinitions.Playlist import Playlist

Logger.Information("Starting Task")

sm = SettingsManager("config.json")
token = Requestor.request_access_token()
responses: list = []

for playlist in sm.proxy_get_appsettings("playlists"):
    responses.append(Playlist(Requestor.get(iid=playlist,
                                            ext="playlists/%s",
                                            token=token)))

generator = Generator()
generator.generate(responses)

Logger.Information("Finished Task")
