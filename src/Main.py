from src import Requestor, Logger, PdfGenerator
from SettingsManager import SettingsManager

Logger.Information("Starting Application")

result = Requestor.get(iid="0rEle8ZGZCOS0dpzi2FgZh", ext="playlists/%s", token=Requestor.request_access_token())

tracks = result["tracks"]
for track in tracks:


Logger.Information("Finished Task")