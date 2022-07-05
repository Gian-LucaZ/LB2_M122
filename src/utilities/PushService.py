import ftplib
from src.utilities import SettingsManager, Logger


def push(file_loc):
    dt = SettingsManager.proxy_get_appsettings("ftp")
    session = ftplib.FTP(dt["server"], dt["id"], dt["secret"])

    Logger.Information("Pushing %s" % file_loc + " to " + dt["server"])

    with open(file_loc, "rb") as file:
        session.storbinary("STOR %s" % file_loc, file)

    file.close()
    session.close()