import yagmail
from src.typedefinitions.Mail import Mail
from src.utilities import Logger, SettingsManager


def SendMail(mail: Mail):
    mc = SettingsManager.proxy_get_appsettings("mail")

    with yagmail.SMTP(mc["id"], mc["secret"]) as yag:
        yag.send(mail.Target, mail.Head, mail.Body)
        Logger.Information("Mail %s sent." % mail.Head)