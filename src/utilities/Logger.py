import datetime
from colorama import Fore, Style
from enum import Enum


def Error(message: str):
    log(message, LogLevel.Error)


def Information(message: str):
    log(message, LogLevel.Information)


def Warning(message: str):
    log(message, LogLevel.Warning)


logfile = open("../log.log", "w")


def log(message: str, log_level):
    now = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"

    match log_level:
        case LogLevel.Error:
            logfile.write(now + " Error: %s" % message)
            print(now + Fore.RED + " Error: " + Style.RESET_ALL + message)
        case LogLevel.Information:
            logfile.write(now + " Debug: %s" % message)
            print(now + Fore.GREEN + " Debug: " + Style.RESET_ALL + message)
        case LogLevel.Warning:
            logfile.write(now + " Warning: %s" % message)
            print(now + Fore.YELLOW + " Warning: " + Style.RESET_ALL + message)

    logfile.write("\n")

class LogLevel(Enum):
    Error = 1
    Information = 2
    Warning = 3
