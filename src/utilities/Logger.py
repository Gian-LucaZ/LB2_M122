import datetime
from colorama import Fore, Style
from enum import Enum


def Error(message: str):
    log(message, LogLevel.Error)


def Information(message: str):
    log(message, LogLevel.Information)


def Warning(message: str):
    log(message, LogLevel.Warning)


def log(message: str, log_level):
    now = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"

    with open("../log.log", "w") as log:
        match log_level:
            case LogLevel.Error:
                log.write(now + " Error: %s" % message)
                print(now + Fore.RED + " Error: " + Style.RESET_ALL + message)
            case LogLevel.Information:
                log.write(now + " Debug: %s" % message)
                print(now + Fore.GREEN + " Debug: " + Style.RESET_ALL + message)
            case LogLevel.Warning:
                log.write(now + " Warning: %s" % message)
                print(now + Fore.YELLOW + " Warning: " + Style.RESET_ALL + message)

    log.close()


class LogLevel(Enum):
    Error = 1
    Information = 2
    Warning = 3
