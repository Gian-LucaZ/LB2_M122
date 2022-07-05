import datetime
from src.utilities import Requestor, Logger
from src.utilities.PdfGenerator import Generator
from src.utilities.SettingsManager import SettingsManager
from src.typedefinitions.Playlist import Playlist
from src.typedefinitions.Mail import Mail
from src.utilities import Messenger

Logger.Information("Starting Task")

sm = SettingsManager("config.json")
token = Requestor.request_access_token()
generator = Generator()

mail = Mail("Playlistfeed of %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sm.proxy_get_appsettings("mail")["target"],
            [])

for id in sm.proxy_get_appsettings("playlists"):
    playlist: Playlist = Playlist(Requestor.get(iid=id,
                                                ext="playlists/%s",
                                                token=token))
    filename: str = generator.generate(playlist)
    mail = Mail("Playlistfeed for " + playlist.name + " (%s)" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                sm.proxy_get_appsettings("mail")["target"],
                [filename])

    Messenger.SendMail(mail)

Logger.Information("Finished Task")
