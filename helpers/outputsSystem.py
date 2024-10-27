from colorama import Fore, Style, init

init(autoreset=True)

def messageError(message):
    print(Fore.RED + Style.BRIGHT + f"ERROR:  {message}" + Style.RESET_ALL)

def messageSuccess(message):
    print(Fore.GREEN + Style.BRIGHT + f"EXITO: {message}" + Style.RESET_ALL)

def messageWarning(message):
    print(Fore.YELLOW + Style.BRIGHT + f"WARNING: {message}" + Style.RESET_ALL)
def sendMessage(message):
    print(Fore.WHITE + Style.BRIGHT + message + Style.RESET_ALL )