import datetime
from src.utilities import Requestor, Logger, PushService, SettingsManager
from src.utilities.PdfGenerator import Generator
from src.typedefinitions.Playlist import Playlist
from src.typedefinitions.Mail import Mail
from src.utilities import Messenger

Logger.Information("Starting Task")

token = Requestor.request_access_token()
generator = Generator()

for id in SettingsManager.proxy_get_appsettings("playlists"):
    playlist: Playlist = Playlist(Requestor.get(iid=id,
                                                ext="playlists",
                                                token=token))
    filename: str = generator.generate(playlist)
    mail = Mail("Playlistfeed for " + playlist.name + " (%s)" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                SettingsManager.proxy_get_appsettings("mail")["target"],
                [filename])

    Messenger.SendMail(mail)
    PushService.push("./%s" % filename)

Logger.Information("Finished Task")
