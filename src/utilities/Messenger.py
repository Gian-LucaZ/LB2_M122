import yagmail
from src.typedefinitions.Mail import Mail
from src.utilities import Logger
from src.utilities.SettingsManager import SettingsManager


def SendMail(mail: Mail):
    sm = SettingsManager("config.json")
    mc = sm.proxy_get_appsettings("mail")

    with yagmail.SMTP(mc["id"], mc["secret"]) as yag:
        yag.send(mail.Target, mail.Head, mail.Body)
        Logger.Information("Mail %s sent." % mail.Head)