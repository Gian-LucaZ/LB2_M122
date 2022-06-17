import datetime
from colorama import Fore, Style
from enum import Enum


def console_log(message: str, log_level):
    now = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"

    match log_level:
        case LogLevel.Error:
            print(now + Fore.RED + " Error: " + Style.RESET_ALL + message)
        case LogLevel.Information:
            print(now + Fore.GREEN + " Info: " + Style.RESET_ALL + message)
        case LogLevel.Warning:
            print(now + Fore.YELLOW + " Warning: " + Style.RESET_ALL + message)


class LogLevel(Enum):
    Error = 1
    Information = 2
    Warning = 3
